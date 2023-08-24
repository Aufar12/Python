***Settings***
Library         SeleniumLibrary          run_on_failure=Nothing


***Variables***
${url}          https://www.dicoding.com/academies/266
${browser}      Chrome
${username}     m.aufar12@gmail.com
${password}     metalchameleon2

***Tasks***
Login Dicoding
    Open Browser    ${url}      ${browser}
    Maximize Browser Window

    Wait Until Element Is Visible           //*[contains(text(),'Masuk')]

    Click Element                           //*[contains(text(),'Masuk')]

    Wait Until Element Is Visible           //*[@id="login_email"]

    Sleep                                   1
    Input Text                              //*[@id="login_email"]              ${username}
    Input Text                              //*[@id="login_password"]           ${password}
    Click Element                           //*[@id="login-modal"]/div/div/div[2]/form/div[3]/button
    # Sleep    1000000000000


Next Process
    # Wait Until Element Is Visible              //*[@id="information"]/div[1]/div/div[2]/div/div/div[1]/a
    # Click Element                              //*[@id="information"]/div[1]/div/div[2]/div/div/div[1]/a
    Sleep     15
    Log To Console    tesssss


    FOR     ${i}    IN RANGE    0   50
        Wait Until Element Is Visible              //*[contains(text(),'Daftar Modul')]

        # Scroll Down


        Wait Until Element Is Visible              //a[contains(text(),'Selanjutnya')]
        Sleep                                       1
        Click Element                               //a[contains(text(),'Selanjutnya')]
    END         


***Keywords***
Scroll Down
    FOR     ${i}    IN RANGE    0   2
        Execute JavaScript                      window.scrollTo(0, document.body.scrollHeight)
        Sleep                                   1
    END

    Execute JavaScript                      window.scrollTo(0, document.body.scrollHeight - 1000)
    
    


