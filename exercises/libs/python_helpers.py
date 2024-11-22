import os
from .helpers import cleanup_files, get_dir, write_to_file, run_and_combine_messsages, run_code

def precheck_python(language, code, precheck_test_cases, passed_tests, numHiddenTestCases):
    try:
        temp_file = os.path.join(get_dir(language), 'student_code.py')           # LẤY FILE CODE CỦA STUDENT
        write_to_file(temp_file, code)                                           # VIẾT CODE VÀO TEMP_FILE THÔNG QUA HÀM write_to_file
        combined_message = run_and_combine_messsages(language, temp_file, None, None, precheck_test_cases, numHiddenTestCases, passed_tests)
        cleanup_files([temp_file])
    except Exception as e:
        return {'error': str(e), 'passed_tests': passed_tests, 'numHiddenTestCases': numHiddenTestCases}
    
    return combined_message

def grade_Python_submission(language, student_code_file, test_cases, passed_tests):        # HÀM CHẤM ĐIỂM
    try:
        for test in test_cases['test_cases']:                                                # DUYÊTJ QUA TỪNG TEST CASE VÀ SO SÁNH
            result = run_code(language, student_code_file, test, None, None) 
            if result.stdout.strip() == test['expected_output'].strip():
                passed_tests += 1
        for hidden in test_cases['hidden_test_cases']:                                       # DUYỆT QUA TỪNG HIDDEN TEST CASE VÀ CHẤM CODE
            hidden_result = run_code(language, student_code_file, hidden, None, None)
            if hidden_result.stdout.strip() == hidden['expected_output'].strip():
                passed_tests += 1
        cleanup_files([student_code_file])
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return  0
    
    return passed_tests