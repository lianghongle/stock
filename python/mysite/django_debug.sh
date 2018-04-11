#!/bin/bash
# 无效？？
show_usage() {
    echo "Usage: `basename` path/to/file"
}
if [ $# != 1 ]
then
    show_usage
    exit -1
fi

datetime=`date +%Y%m%d%H%i%s`
tmp_file="tmp_debug_python_script_$datetime.py"
script_path=$1
script_path=${script_path%\.py}
script_path=${script_path//\//.}

echo "import os" >> $tmp_file
echo "os.environ['MODULE_DEBUG']='on'" >> $tmp_file
echo "import $script_path">> $tmp_file
cat $tmp_file|python3 manage.py shell

rm $tmp_file