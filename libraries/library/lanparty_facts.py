from ansible.module_utils.basic import AnsibleModule
from os.path import isfile, isdir

def main():

    facts = {}

    module = AnsibleModule(
        argument_spec = dict()
    )

    # Gather cpufreq and available governors into 'facts'
    sysfs_path = '/sys/devices/system/cpu/cpu0'
    cpufreq_facts(facts, sysfs_path)

    module.exit_json(changed=False, ansible_facts=facts)

# Emits the following facts:
# - ansible_cpufreq - bool
# - ansible_governors - list of supported governors
def cpufreq_facts(facts, sysfs_path):

    cpufreq_enabled = isdir('{}/cpufreq'.format(sysfs_path))
    cpufreq_governors = []

    if cpufreq_enabled:
        with open('{}/cpufreq/scaling_available_governors'.format(sysfs_path)) as gov:
            gs = gov.read().rstrip()
            cpufreq_governors = gs.split(' ')

    facts['ansible_cpufreq'] = cpufreq_enabled
    facts['ansible_governors'] = cpufreq_governors

if __name__ == '__main__':
    main()
