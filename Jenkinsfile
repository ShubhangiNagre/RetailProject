pipeline {
    agent any

    environment {
        JAVA_HOME = '/opt/bitnami/java'
        PATH = "${env.JAVA_HOME}/bin:${env.PATH}"
    }

    stages {
        stage('Setup Virtual Environment') {
            steps {
                script {
                    // Create virtual environment and install pipenv
                    sh '''
                        python3 -m venv retail_pipeline_venv
                        ./retail_pipeline_venv/bin/pip install --upgrade pip
                        ./retail_pipeline_venv/bin/pip install pipenv
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh './retail_pipeline_venv/bin/pipenv install'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Check environment variables and run tests
                    sh '''
                        echo $JAVA_HOME
                        echo $PATH
                        ./retail_pipeline_venv/bin/pipenv run pytest
                    '''
                }
            }
        }

        stage('Package') {
            steps {
                script {
                    sh 'zip -r retailproject.zip . -x "retail_pipeline_venv/*"'
                }
            }
        }

        stage('Deploy') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'labcreds', usernameVariable: 'LABS_USR', passwordVariable: 'LABS_PSW')]) {
                    sh '''
                        sshpass -p "$LABS_PSW" scp -o StrictHostKeyChecking=no -r \
                        retailproject.zip $LABS_USR@g01.itversity.com:/home/$LABS_USR/retailproject
                    '''
                }
            }
        }
    }
}
