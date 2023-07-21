import sys

def get_params():

    l_args = sys.argv[1:]

    # d_params = dict( scope = 'local', pkg_mgr = 'npm' )
    d_params = dict( scope = 'global', pkg_mgr = 'pnpm', type='basic' )
    d_options = dict( scope = ['global','local'], pkg_mgr = ['npm','pnpm'], type=['basic','website'] )

    for arg in l_args:
        if arg.__contains__('--') and arg.__contains__('='):
            arg = arg.strip('--')
            key, value = arg.split('=')
            if key in d_params and value in d_options[key]:
                d_params[key] = value
                continue

        print(f'\n    Arg : {arg} is not valid\n\n    Params must be:')
        for key in d_params.keys():
            values = ' or '.join(d_options[key])
            print(f'        --{key}={values}')
        print()
        sys.exit()
    else:
        return d_params