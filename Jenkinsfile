pipeline {
    agent any

    stages {
        stage('Cloning') {
            steps {
                echo 'I am cloning git branch..'
                git 'https://github.com/ashwaqar/my_scripts.git'
            }
        }
        stage('Run') {
            steps {
                echo 'runnning list.sh ..'
                sh label: 'Running list', script: 'sudo sh list.sh'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing....'
                fileExists 'shell_results.txt'
            }
        }
    }
}
