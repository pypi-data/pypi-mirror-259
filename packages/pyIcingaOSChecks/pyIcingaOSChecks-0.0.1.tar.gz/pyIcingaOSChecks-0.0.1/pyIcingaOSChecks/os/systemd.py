from pyIcingaFramework.check import IcingaCheck, Measurement
from pyIcingaFramework.utils import convertDataUOM
import logging
import dbus


class Systemd(IcingaCheck):

    def check(self, **kawrgs):

        filters = self._parseFilters(required_filters='unit')

        systemd_unit_list = filters['unit'].split(',')

        ###################################
        # Gather Data
        ###################################

        data = {}
        bus = dbus.SystemBus()
        systemd1 = bus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
        manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')

        for unit in systemd_unit_list:

            ###################################
            # Set Thresholds
            ###################################

            self.set_threshold('~%active', '~%active', label=f'{unit}_activeState')
            self.set_threshold('~%running', '~%running', label=f'{unit}_subState')


            try:
                service = bus.get_object('org.freedesktop.systemd1', object_path=manager.GetUnit(unit))

                interface = dbus.Interface(service, dbus_interface='org.freedesktop.DBus.Properties')

                data[unit] = {} 
                data[unit]['activeState'] = interface.Get('org.freedesktop.systemd1.Unit', 'ActiveState')
                data[unit]['subState'] = interface.Get('org.freedesktop.systemd1.Unit', 'SubState')


            except dbus.exceptions.DBusException:
                data[unit] = {'activeState': 'unloaded', 'subState': 'not running'}

            ###################################
            # Add Measurements
            ###################################
            self.result.add_measurement(f'{unit}_activeState', data[unit]['activeState'], warning=self.get_threshold('warning', f'{unit}_activeState'), critical=self.get_threshold('critical', f'{unit}_activeState'), is_perf=False, alerts=True)  # pylint: disable=no-member
            self.result.add_measurement(f'{unit}_subState', data[unit]['subState'], warning=self.get_threshold('warning', f'{unit}_subState'), critical=self.get_threshold('critical', f'{unit}_subState'), is_perf=False, alerts=True)   # pylint: disable=no-member
   


        ###################################
        # Set Status
        ###################################
        

        status_code = 0
        # Set stdout messages
        logging.info('checking thresholds...')
        for measurement in self.result.measurements:
            logging.debug('check measurement %s for breaches' % measurement.label)
            statusCode = measurement.status()
            if statusCode > status_code:
                status_code = int(statusCode)

        logging.info('Creating stdout msg...')


        ###################################
        # Format output
        ###################################
                
        output_text = []
        output_text.append("Systemd Unit Status")

        for unit_name, unit_properties in data.items():
            activeState_statusCode = self.result.get_measurement(f'{unit_name}_activeState').status()
            logging.debug(activeState_statusCode)
            subState_statusCode = self.result.get_measurement(f'{unit_name}_subState').status()

            status = 'OK'
            if activeState_statusCode > 0 or subState_statusCode > 0:
                status = 'CRITCIAL'

            output_text.append(f"\_ [{status}] Unit {unit_name} ({unit_properties['activeState']}) - {unit_properties['subState']}")

        self.result.stdout = '\n'.join(output_text)

        return self.result
