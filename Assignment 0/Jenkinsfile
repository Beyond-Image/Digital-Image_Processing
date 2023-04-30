pipeline {
    agent { docker { image 'pmantini/assignment-cosc6380:latest' } }

    environment {
        PATH = "env/bin/:$PATH"
    }
    stages {
        stage('build') {
            steps {
                sh 'python dip_hw0.py -ic color_image.png -ib blackwhite_image.png -c 149'
                sh 'python dip_hw0.py -ic color_image.png -ib blackwhite_image.png -c 50'
                sh 'python dip_hw0.py -ic color_image.png -ib blackwhite_image.png -t 180 -tc 0 -tc 255 -tc 0'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'output/**/*.* ', onlyIfSuccessful: true
        }
    }
}