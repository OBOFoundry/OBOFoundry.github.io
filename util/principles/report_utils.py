#!/usr/bin/env python3

import os
import subprocess
import time

from dash_utils import format_msg
from py4j.protocol import Py4JJavaError


def run_report(robot_gateway, io_helper, ns, ontology):
    """Run and return a ROBOT Report.

    Args:
        robot_gateway (Gateway): py4j gateway to ROBOT
        io_helper (IOHelper): ROBOT IOHelper
        ns (str): ontology namespace
        ontology (OWLOntology): ontology object

    Return:
        ROBOT Report object
    """
    if ontology is None:
        return None

    report_options = robot_gateway.ReportOperation.getDefaultOptions()
    report_options['labels'] = 'true'

    # run the report
    report = None
    try:
        report = robot_gateway.ReportOperation.getReport(
                ontology, io_helper, report_options)
    except Py4JJavaError as err:
        msg = err.java_exception.getMessage()
        print('REPORT FAILED\n' + str(msg))
        return None

    return report


class BigReport:
    """Helper class to run a Report over a large ontology. Report queries are
    run over a dataset on disk instead of in memory.
    """
    def __init__(self, robot_gateway, ns, file):
        """Instantiate a new BigReport object by running a report over the
        ontology file.
        """
        tdb_dir = 'build/.%s-tdb' % ns
        report_options = robot_gateway.ReportOperation.getDefaultOptions()
        report_options['tdb-directory'] = tdb_dir
        report_options['keep-tdb-mappings'] = 'true'
        report_options['limit'] = '1'
        report_options['tdb'] = 'true'
        report = None

        self.good_format = True
        try:
            print('Loading triples to %s and running report...' % tdb_dir)
            report = robot_gateway.ReportOperation.getTDBReport(
                file, report_options)
        except Py4JJavaError as err:
            msg = err.java_exception.getMessage()
            print('REPORT FAILED\n' + str(msg))
            self.report = None
            if 'cannot be read' in msg:
                self.good_format = False

        self.report = report

    def get_report(self):
        """Return the Report object.
        """
        return self.report

    def get_good_format(self):
        """Return True if the file provided is valid RDF/XML that can be loaded
        by Jena.
        """
        return self.get_good_format


def run_big_report(robot_gateway, ns, file):
    """Run a Report over a big ontology and return the Report object.
    This is suited for big ontologies as the Report queries are run over a
    dataset on disk instead of in memory.

    Args:
        robot_gateway (Gateway): py4j gateway to ROBOT
        ns (str): ontology namespace
        file (str): path to ontology file

    Returns:
        Report object
    """
    tdb_dir = 'build/.%s-tdb' % ns
    report_options = robot_gateway.ReportOperation.getDefaultOptions()
    report_options['tdb-directory'] = tdb_dir
    report_options['keep-tdb-mappings'] = 'true'
    report_options['limit'] = '10000'
    report_options['tdb'] = 'true'
    report = None
    try:
        print('Loading triples to %s and running report...' % tdb_dir)
        report = robot_gateway.ReportOperation.getTDBReport(
            file, report_options)
    except Py4JJavaError as err:
        msg = err.java_exception.getMessage()
        print('REPORT FAILED\n' + str(msg))
        return None
    return report


def process_report(robot_gateway, ns, report):
    """Save the Report and return the status.

    Args:
        robot_gateway (Gateway): py4j gateway to ROBOT
        ns (str): ontology namespace
        report (Report): completed Report object

    Return:
        ERROR, WARN, INFO, or PASS with optional help message
    """
    if report is None:
        return 'INFO|report failed'
    outfile = 'reports/robot/%s.tsv' % ns

    # print summary to terminal and save to report file
    report_options = robot_gateway.ReportOperation.getDefaultOptions()
    robot_gateway.ReportOperation.processReport(
        report, outfile, report_options)
    print('See %s for details\n' % outfile)

    # return the report status
    errs = report.getTotalViolations('ERROR')
    warns = report.getTotalViolations('WARN')
    info = report.getTotalViolations('INFO')

    if errs > 0:
        return format_msg('ERROR', ['{0} errors'.format(errs),
                                    '{0} warnings'.format(warns),
                                    '{0} info messages'.format(info),
                                    'Click to download report'])
    elif warns > 0:
        return format_msg('WARN', ['{0} warnings'.format(warns),
                                   '{0} info messages'.format(info),
                                   'Click to download report'])
    elif info > 0:
        return format_msg('INFO', ['{0} info messages'.format(info),
                                   'Click to download report'])
    else:
        return 'PASS'
