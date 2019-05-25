import xmltodict


def main():
    '''
    report.xml is generated from pytest --junitxml=report
    '''
    with open('./report.xml', 'r') as file:
        test_result = file.read()
        test_result_dict = xmltodict.parse(test_result)
        total_time = test_result_dict['testsuite']['@time']
        for testcase in test_result_dict['testsuite']['testcase']:
            class_name = testcase['@classname']
            file_name= testcase['@file']
            test_name = testcase['@name']
            test_time = testcase['@time']

            print(f'{class_name}.{test_name}: {test_time}')

main()
