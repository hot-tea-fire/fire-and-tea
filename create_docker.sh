
if docker ps -a | grep -i 'fire_tea'; then
   docker rm -f 'fire_tea'
else
   echo "fire_tea 不存在"
fi

docker build -t test_log:1.0 .

docker run -itd --privileged=true --restart=always --gpus all -v /package/yucenpu:/package/yucenpu -p 3860:3860 -p 6321:6321 --name test_log test_log:1.0
