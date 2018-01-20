"""A very janky script to verify all the solutions."""

import os

errors = 0

for p in range(1, 19):
    errors += os.system('git diff {0}/my_output.txt {0}/Prob{0}.out.txt'.format(str(p).zfill(2)))

if errors == 0:
    print('All solutions match their expected values.')
else:
    print('Some solutions are not as expected, though it is possible this was cause by line endings. There will be '
          'output above this message from git diff if there are indeed significant differences.')
