pipeline {
    agent any
    // In additional to manual runs, trigger somewhere at midnight to
    // give us the max time in a day to get things right.
    triggers {
	// Master never runs--Feb 31st.
	cron('0 0 31 2 *')
	// Nightly @12am.
	//cron('0 0 2-31 * *')
	// First of the month @12am, for "release" (also "current").
	//cron('0 0 1 * *')
    }
    environment {
	///
	/// Automatic run variables.
	///

	// Pin dates and day to beginning of run.
	START_DATE = sh (
	    script: 'date +%Y-%m-%d',
	    returnStdout: true
	).trim()

	START_DAY = sh (
	    script: 'date +%A',
	    returnStdout: true
	).trim()

	///
	/// Internal run variables.
	///

	// The people to call when things go bad. It is a comma-space
	// "separated" string.
	TARGET_ADMIN_EMAILS = 'rbca.jackson@gmail.com'
	TARGET_SUCCESS_EMAILS = 'rbca.jackson@gmail.com'
	// Control make to get through our loads faster if
	// possible. Assuming we're cpu bound for some of these...
	// wok has 48 "processors" over 12 "cores", so I have no idea;
	// let's go with conservative and see if we get an
	// improvement.
	//MAKECMD = 'make --jobs 3 --max-load 10.0'
	MAKECMD = 'make'
    }
    options{
	timestamps()
	buildDiscarder(logRotator(numToKeepStr: '14'))
    }
    stages {
	// Very first: pause for a minutes to give a chance to cancel
	// and clean the workspace before use.
	stage('Ready and clean') {
	    steps {
		// Give us a minute to cancel if we want.
		//sleep time: 1, unit: 'MINUTES'
		cleanWs deleteDirs: true, disableDeferredWipeout: true
	    }
	}
	stage('Initialize') {
	    steps {
		// Start preparing environment.
		sh 'env > env.txt'
		sh 'echo $BRANCH_NAME > branch.txt'
		sh 'echo "$BRANCH_NAME"'
		sh 'cat env.txt'
		sh 'cat branch.txt'
		sh 'echo $START_DAY > dow.txt'
		sh 'echo "$START_DAY"'
	    }
	}
	// Our main bit of work.
	stage('Produce ontology') {
	    agent {
		docker {
		    image 'obolibrary/odkfull:v1.1.7'
		    // Reset Jenkins Docker agent default to original
		    // root.
		    args '-u root:root'
		}
	    }
	    steps {

		// Create a relative working directory and setup our
		// working environment.
		dir('./OBOFoundry.github.io') {
		    git branch: BRANCH_NAME,
			url: 'https://github.com/OBOFoundry/OBOFoundry.github.io'

		    // Setup our environment the way we want.
		    sh 'pip3 install -r requirements.txt'
		    sh 'apt-get -f install lsof'
		    sh 'apt-get -f install zip'

		    // Check what our world looks like.
		    sh 'env'

		    // We're downloading things, so lets give it a few
		    // tries.
                    timeout(time: 8, unit: 'HOURS') {
			retry(3){
			    sh 'export PYTHONUNBUFFERED=1'
			    sh '$MAKECMD clean-dashboard'
			}
		    }
                }
	    }
	}
    }
    post {
	// On success, archive our stuff and let our general public
	// people know things went well.
    	success {
                archiveArtifacts artifacts: 'reports/*.zip', fingerprint: true
    	    script {
        		echo "There has been a successful run of the ${env.BRANCH_NAME} pipeline."
        		mail bcc: '', body: "There has been successful run of the ${env.BRANCH_NAME} pipeline. Please see: https://build.obolibrary.io/job/obofoundry/job/pipeline/job/${env.BRANCH_NAME}", cc: '', from: '', replyTo: '', subject: "OBO pipeline success for ${env.BRANCH_NAME}", to: "${TARGET_SUCCESS_EMAILS}"
    	    }
    	}
    	// Let's let our internal people know if things change.
            changed {
        	    echo "There has been a change in the ${env.BRANCH_NAME} pipeline."
        	    mail bcc: '', body: "There has been a pipeline status change in ${env.BRANCH_NAME}. Please see: https://build.obolibrary.io/job/obofoundry/job/pipeline/job/${env.BRANCH_NAME}", cc: '', from: '', replyTo: '', subject: "OBO pipeline change for ${env.BRANCH_NAME}", to: "${TARGET_ADMIN_EMAILS}"
    	}
    	// Let's let our internal people know if things go badly.
    	failure {
    	    echo "There has been a failure in the ${env.BRANCH_NAME} pipeline."
    	    mail bcc: '', body: "There has been a pipeline failure in ${env.BRANCH_NAME}. Please see: https://build.obolibrary.io/job/obofoundry/job/pipeline/job/${env.BRANCH_NAME}", cc: '', from: '', replyTo: '', subject: "OBO pipeline FAIL for ${env.BRANCH_NAME}", to: "${TARGET_ADMIN_EMAILS}"
        }
    }
}
