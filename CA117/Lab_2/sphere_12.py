print('Radius (m)      Area (m^2)    Volume (m^3)','\n'+'-'*10+' '*6+'-'*10+' '*4+'-'*12,*(lambda p,a,b,c:['\n{:>10.1f}{:>16.2f}{:>16.2f}'.format(x*b,4*p*((x*b)**2),(float(4)/3)*p*((x*b)**3))for x in range(int(a),int((c+b)/b))])(__import__('math').pi,*[float(x)for x in __import__('sys').argv[1:]]))