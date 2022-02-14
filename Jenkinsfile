pipeline {

    agent any

    stages {

        stage('get_commit_details') {
                steps {
                    script {
                        env.GIT_COMMIT_MSG = sh (script: 'git log -1 --pretty=%B ${GIT_COMMIT}', returnStdout: true).trim()
                        env.GIT_AUTHOR = sh (script: 'git log -1 --pretty=%cn ${GIT_COMMIT}', returnStdout: true).trim()
                        echo ${env.GIT_AUTHOR}
                        echo ${env.GIT_COMMIT_MSG}
                    }
                }
            }
        }
}