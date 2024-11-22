import os
import subprocess
import re

from django.conf import settings


def get_dir(language):  # LẤY ĐƯƠNGF DẪN ĐẾN NGÔN NGỮ
    EXERCISE_DIR = os.path.normpath(os.path.join(settings.BASE_DIR, 'exercise_files')) #EXERCISE_DIR LÀ "C:\Users\Trong Tin\Desktop\LMS-FSA-truong-dev\exercises"   
    os.makedirs(EXERCISE_DIR, exist_ok=True)
    if language == 'python':
        return os.path.normpath(os.path.join(EXERCISE_DIR, 'python_files'))
    elif language == 'c':
        return os.path.normpath(os.path.join(EXERCISE_DIR, 'c_files'))
    elif language == 'java':
        return os.path.normpath(os.path.join(EXERCISE_DIR, 'java_files'))
    else:
        raise ValueError(f"Unsupported language: {language}")

def prepare_file_paths(language, student_code):   # TÌM KIẾM FILE STUDENT CODE ĐỂ GHÉP LINK VỚI PATH LANGUAGE , NẾU LÀ PYTHON THÌ THỰC THI TRỰC TIẾP FILE PY
                                                  # C THÌ CẦN BIÊN DỊCH TRƯỚC KHI RUN NÊN PHẢI CHUYỂN SANG EXE
                                                  # JAVA THÌ CẦN TÌM CHUỖI KHỚP VỚI PUBLIC CLASS SAU ĐÓ LẤY LÊN VÀ GÁN VÀO TÊN FILE JAVA
    try:
        if language == 'python':
            student_code_file = os.path.join(get_dir(language), 'student_code.py')
            return student_code_file, "no_executable_needed", "no_class_name"
        elif language == 'c':
            student_code_file = os.path.join(get_dir(language), 'student_code.c')
            compiled_executable = os.path.join(get_dir(language), 'student_program.exe')
            return student_code_file, compiled_executable, "no_class_name"
        elif language == 'java':
            match = re.search(r'public\s+class\s+(\w+)', student_code)
            if match:
                class_name = match.group(1)
                student_code_file = os.path.join(get_dir(language), f"{class_name}.java")
                return student_code_file, "no_executable_needed", class_name
            else:
                return "no_file_path", "no_executable_needed", "unknown_class"
    except Exception as e:
        print(e)

def write_to_file(file_path, content):              # OPEN FILE WRITE CONTENT
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def calculate_score(passed_tests, total_tests):
    return (passed_tests / total_tests) * 100 if total_tests > 0 else 100

def cleanup_files(file_paths):         # NẾU CÓ FILE TỒN TẠI TRƯỚC ĐÓ THÌ XÓA NÓ ĐI
    for file_path in file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)
        # else:
        #     print(f"File {file_path} does not exist, cannot delete.")

def run_code(language, test_file, test, compiled_executable, class_name):    # TEST_FILE : Đường dẫn đến tệp mã nguồn cần chạy đối với Python.
                                                                             # TEST CHO PYTHON
                                                                             # COMPILED_ỄCUTABLE CHO C
                                                                             # CLASS_NAME CHO JAVA 
    match language:
        case 'python':
            command = ['python', test_file]
        case 'c':
            command = compiled_executable
        case 'java':
            command = ['java', '-cp', get_dir('java'), class_name]
    result = subprocess.run(                                                  # SUBPROCESS DÙNG ĐỂ CHẠY CHƯƠNG TRÌNH BÊN NGOÀI HOẶC SHELL
        command,                                                              # STDOUT : OUTPUT
        input=test['input'],                                                  # STDERR : EROR
        capture_output=True,    # GHI LẠI ĐẦU RA
        text=True       # TRẢ VỀ TEXT THAY VÌ BYTE
    )
    return result

def run_and_combine_messsages(language, test_file, compiled_executable, class_name, precheck_test_cases, numHiddenTestCases, passed_tests):
    message = []
    try:
        for test in precheck_test_cases:
            message_temp = ""
            # Run the student_code.py script via subprocess
            try:
                result = run_code(language, test_file, test, compiled_executable, class_name)
                output = result.stdout       # CHẠY CODE LẤY OUTPUT
            except:
                output = ""
            message_temp += f"<strong>Your Result:</strong>" + "&nbsp;&nbsp;&nbsp;&nbsp;" +str(output) + "<br>"
            message_temp += f"<strong>Expected Result:</strong>" + "&nbsp;&nbsp;&nbsp;&nbsp;" +str(test['expected_output'].strip()) + "<br>"
            if output.strip() == test['expected_output'].strip():  # SO SÁNH OUTPUT VÀ TEST CASE
                passed_tests += 1
                # Thêm nội dung vào thẻ alert success khi pass
                message.append(
                    f'<div class="alert alert-success" role="alert">'
                    f'{message_temp}<div style="text-align: center;"><strong>&lt;&lt;&lt;&lt;&lt;&lt; Pass &gt;&gt;&gt;&gt;&gt;&gt;</strong></div>'
                    f'</div>'
                )
            else:
                error_msg = "Please check the expected Result !!!"
                # Thêm nội dung vào thẻ alert danger khi fail
                message.append(
                    f'<div class="alert alert-danger" role="alert">'
                    f'{message_temp} <div style="text-align: center;"><strong>{error_msg}</strong><br><strong>&lt;&lt;&lt;&lt;&lt;&lt; Fail &gt;&gt;&gt;&gt;&gt;&gt;</strong></div>'
                    f'</div>'
                )
            # PHẦN HIỂN THỊ TEST CASE BÊN PHẢI 
            header_msg = f"""
            <div style="text-align: center;">
            <h5> <span style="color: white;"> &lt;&lt;&lt;&lt;&lt;RUNNING TEST CASES&gt;&gt;&gt;&gt;&gt;</span></h5>              
            <h6> <span style="color: red;">You have passed {passed_tests} test cases.<br>                                
            {numHiddenTestCases} HIDDEN TEST CASES LEFT. </span></h6></div><br>
            
            """
        message.insert(0, header_msg)
    except subprocess.CalledProcessError as e:
        return {'error': f"Error: {e}"}
    combined_message = ''.join(message)
    return combined_message
