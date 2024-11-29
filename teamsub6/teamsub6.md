### [팀 과제] (6) Jenkins Pipeline을 이용한 빌드 및 배포


1) Jenkins 컨테이너 생성
Host Docker CLI 와 Jenkins Docker CLI 의 Docker Socket 을 공유하여 Jenkins 컨테이너에서 Host 에 Application Container 를 생성할 수 있도록 연결
(Host Shell 에서 명령어 실행)
```sh
docker run -d --name Teamsub6-Jenkins -p 8080:8080 -v /home/jenkins:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -u root jenkins/jenkins:lts
```

2) Jenkins 컨테이너 내부에 docker 설치
(Jenkins Container Shell 에서 명령어 실행)
```sh
apt update && \
apt install -y ca-certificates curl gnupg lsb-release && \
mkdir -p /etc/apt/keyrings && \
curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
apt update && \
apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

3) Jenkins 컨테이너 내부에 Application 설치
(Jenkins Container Shell 에서 명령어 실행)
```sh
mkdir -p /var/jenkins_home/workspace
git clone https://github.com/CSID-DGU/2024-2-OSSPrac-openmind-08.git /var/jenkins_home/workspace/prac12py
```

4) Jenkins 컨테이너를 dockerhub 에 push
(Host Shell 에서 명령어 실행)
```sh
docker commit prac12_c openmind/jenkins
docker push openmind/jenkins:1.0
```

5) Jenkins password 확인
(Jenkins Container Shell 에서 명령어 실행)
```sh
cat /var/jenkins_home/secrets/initialAdminPassword
```