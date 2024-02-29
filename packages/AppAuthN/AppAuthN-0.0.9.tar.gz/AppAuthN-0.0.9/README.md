# AppAuthN

`AppAuthN` 是一個用於驗證 xApp 身份的 Python 模塊。

## 使用方法

1. download package:

    ```bash
   pip install AppAuthN
    
2. 進行註冊

    ```python
    #模型
    import CertificationReceiver as register
    api = <url>
    register.kongapi(api)

    register_data = {
        "application_token": "1234",
        "position_uid": "6543",
        "inference_client_uid": "5678"
    }
    register.send_register_request(register_data)

3. 進行推論：

   ```python
    #模型
    import InferenceResult as inference
    raw_data = {
        "application_uid": <application_uid>,
        "position_uid": <position_uid>,
        "inference_client_uid": <inference_client_uid>,
        "value": <value>
    }
    inference.send_rawdata(raw_data)

# 注意事项

-請確保提供有效的输入，否則驗證可能會失败。
