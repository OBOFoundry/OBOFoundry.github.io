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
	}
}
