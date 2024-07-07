#Exercise 6-7 page 111
people = {
    'lsumrall':{
        'first':'lester',
        'last':'sumrall',
        'born':'lousiana',
        'job':'preacher',
        'location':'pensecola',
    },
    'ccarnegy':{
        'first':'dale',
        'last':'carnegy',
        'born':'new york',
        'job':'eunterprenuer',
        'location':'penselvania',
    },
}
for username,user_info in people.items():
    print(f"\nUsername :{username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    born_job = f"{user_info['born']+":"} {user_info['job']}"
    location = user_info['location']
    print(f"\tFull name:{full_name.title()}")
    print(f"Born and job:{born_job.title()}")
    print(f"Location:{location.title()}")
