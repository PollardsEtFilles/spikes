
import pip

for m in sorted(["%s==%s" % (i.key, i.version) for i in pip.get_installed_distributions()]):
    print(m)
