import os
import re

import pip

installed_packages = pip.get_installed_distributions()
installed_packages = {i.key: i.version for i in installed_packages}
file_pattern = re.compile(r'\w+\.txt')
package_pattern = re.compile(r'[\w-]+==\d+\.\d+(\.\d)?')
files = [file for file in os.listdir('../requirements/') if file_pattern.match(file)]
print(files)
files = ['../requirements/'+file for file in files]
for file in files:
    with open(file, 'r') as f:
        packages = f.readlines()
    for i, package in enumerate(packages):
        package = package.strip()
        if package_pattern.match(package):
            name, version = package.split('==')
            try:
                old_version = version
                version = installed_packages[name]
                if old_version != version:
                    print('Updated {} from {} to {} in file {}'.format(name, old_version, version, file))
            except KeyError:
                pass
            package = '{}=={}'.format(name, version)
        packages[i] = package
    with open(file, 'w') as f:
        f.write('\n'.join(packages))
        f.write('\n')
