pipeline {
    agent any

    environment {
        LABS = credentials('labcreds')

    }

    stages {
        stage('Build') {
            steps {
                script {
                    sh '''
                        pip3 install --user pipenv
                        /bitnami/jenkins/home/.local/bin/pipenv --rm || true
                        /bitnami/jenkins/home/.local/bin/pipenv install
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh '/bitnami/jenkins/home/.local/bin/pipenv run pytest'
                }
            }
        }

        stage('Package') {
            steps {
                script {
                    sh 'zip -r retailproject.zip .'
                }
            }
        }

        stage('Deploy') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'labcreds', usernameVariable: 'LABS_USR', passwordVariable: 'LABS_PSW')]) {
                    script {
                        sh '''
                            sshpass -p "$LABS_PSW" scp -o StrictHostKeyChecking=no -r \
                            retailproject.zip $LABS_USR@g01.itversity.com:/home/$LABS_USR/retailproject
                        '''
                    }
                }
            }
        }
    }
}
