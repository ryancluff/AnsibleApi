# from ansible_runner import Runner, RunnerConfig

# # Using tag using RunnerConfig
# rc = RunnerConfig(
#     private_data_dir="plays",
#     playbook="chimaera.yml",
#     tags='drain',

# )

# rc.prepare()
# rc.
# r = Runner(config=rc)
# r.run()

import ansible_runner

r = ansible_runner.run(
    private_data_dir="plays",
    playbook="chimaera.yml",
    inventory=[
        'common',
        'cluster0'
    ],
    tags='uncordon',
    cmdline='--vault-password-file .vault_pass'
)

print("{}: {}".format(r.status, r.rc))
# successful: 0
for each_host_event in r.events:
    print(each_host_event['event'])
print("Final status:")
print(r.stats)
