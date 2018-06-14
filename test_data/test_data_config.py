# -*- coding:utf-8 -*-


class GlobalVar:
    case_id = 0
    case_name = 1
    host = 2
    url = 3
    run_status = 4
    method = 5
    header_file = 6
    header_key = 7
    body_file = 8
    body_key = 9
    depend_case = 10
    depend_data = 11
    depend_key = 12
    expect = 13
    result = 14


def get_caseID_col():
    return GlobalVar.case_id


def get_caseName_col():
    return GlobalVar.case_name


def get_host_col():
    return GlobalVar.host


def get_url_col():
    return GlobalVar.url


def get_runStatus_col():
    return GlobalVar.run_status


def get_method_col():
    return GlobalVar.method


def get_header_file_col():
    return GlobalVar.header_file


def get_header_key_col():
    return GlobalVar.header_key


def get_body_file_col():
    return GlobalVar.body_file


def get_body_key_col():
    return GlobalVar.body_key


def get_depend_case_col():
    return GlobalVar.depend_case


def get_depend_data_col():
    return GlobalVar.depend_data


def get_depend_key_col():
    return GlobalVar.depend_key


def get_expect_col():
    return GlobalVar.expect


def get_result_col():
    return GlobalVar.result