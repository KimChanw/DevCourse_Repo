def convert_decimal_to_hex(decimal_num):
    """
    10진수를 16진수로 변환하는 함수
    
    parameter:
    decimal_num : 10진수 숫자
    """
    
    # 16진수를 나타내는 0x를 문자열에서 제거 후 대문자화하여 return
    hex_num = hex(decimal_num).replace('0x', '')
    return hex_num.upper()

