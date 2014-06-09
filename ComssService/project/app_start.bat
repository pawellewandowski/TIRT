start cmd /k "cd decision_maker1 & python decision_maker_service1.py"
Timeout 1
start cmd /k "cd decision_maker2 & python decision_maker_service2.py"
Timeout 1
start cmd /k "cd decision_maker3 & python decision_maker_service3.py"
Timeout 1
start cmd /k "cd bayes_classifier & python bayes_classifier_service.py"
Timeout 1
start cmd /k "cd injection_classifier & python injection_classifier_service.py"
Timeout 1
start cmd /k "cd mail_classifier & python mail_classifier_service.py"
Timeout 1
start cmd /k "cd http_extractor & python http_extractor_service.py"
Timeout 1
start cmd /k "cd byte_extractor & python byte_extractor_service.py"
Timeout 1
start cmd /k "cd address_extractor & python address_extractor_service.py"
Timeout 1
start cmd /k "cd mail_extractor & python mail_extractor_service.py"
Timeout 1
start cmd /k "cd log_analyzer & python log_analyzer_service.py"
Timeout 1
start cmd /k "cd servers_emulator & python servers_emulator_service.py"
Timeout 1
start cmd /k "cd servers_emulator & python sender_http.py"
Timeout 1
start cmd /k "cd servers_emulator & python sender_smtp.py"