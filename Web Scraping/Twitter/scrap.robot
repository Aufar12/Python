*** Settings ***
Documentation   Scraping Twitter
Library         SeleniumLibrary        run_on_failure=Nothing
Library         BuiltIn
Library         DateTime
Library         Process
Library         OperatingSystem
Library         Collections
Library		    custfunc.py
Library         Reserved

*** Tasks ***
Scraping Twitter Thread
    Open Browser            https://twitter.com/i/flow/login      Chrome
    Login Twitter
    @{list_thread}                          Create List        https://twitter.com/convomfs/status/1493821270534008832     https://twitter.com/WidyoLita/status/1288676171861770242    https://twitter.com/yusril_kurzah/status/1288709928752824320    https://twitter.com/remukanbakwan__/status/1288845902422056961    https://twitter.com/nksthi/status/1288638758821040128     https://twitter.com/panjidorky13/status/1289050938607407107     https://twitter.com/Felizersyhy/status/1288660407817629696     https://twitter.com/kholidpurnomoaj/status/1288854395359174659 
    @{list_target}                          Create List        @convomfs        @WidyoLita        @yusril_kurzah    @remukanbakwan__    @nksthi    @panjidorky13    @Felizersyhy    @kholidpurnomoaj
    Set Global Variable                     @{list_thread}
    Set Global Variable                     @{list_target}
    Scraping Data Like & Retweet
    # Scraping Reply

*** Keywords ***
Login Twitter
    Maximize Browser Window         
    Wait Until Element Is Visible           //input                                 20
    Input Text                              //input                                 @AyuhmDyah
    Click Element                           //span[contains(text(),"Next")]
    Wait Until Element Is Visible           //input[@type='password']               20
    Input Password                          //input[@type='password']               dyahayuhm26
    Click Element                           //span[contains(text(),"Log")]          
    Wait Until Element Is Visible           //div[contains(text(),"happening")]     20

Scraping Data Like & Retweet
    @{list_like}                            Create List
    @{list_retweet}                         Create List

    FOR  ${i}  IN   @{list_thread}
        Go To                               ${i}
        Sleep                               10
        ${status}          Run keyword and Return Status     Wait Until Element Is Visible        //a[@href='/login']        10
        Run Keyword If    '${status}'=='True'    Reload Page
        Wait Until Element Is Visible       //article[@role="article"]            20
        Click Element                       //span[contains(text(),"Suka") or contains(text(),"Like")]
        ${temp_list}                        Scrap All User Like & Retweet
        Append To List         ${list_like}           ${tempList}
        Click Element                       //span[contains(text(),"Retweet")]
        ${temp_list}                        Scrap All User Like & Retweet
        Append To List         ${list_retweet}        ${tempList}
    END

    Scrap To Excel    ${list_target}      ${list_like}      ${list_retweet}


Scrap All User Like & Retweet

    Wait Until Element Is Visible    //*[@id="layers"]//section/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div/a/div/div/span     20

    @{list_akun}        Create List
    
    FOR     ${j}        IN RANGE    1       501
        Log To Console     ${j}
        ${elements}        Get WebElements        //*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/section/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div/a/div/div/span
        ${tempList}        Scrap Account          ${elements} 
        Append To List     ${list_akun}           ${tempList}
        Scroll Menu        15
        Scroll Menu Up     3
        Sleep              1.5
    END
    
    Log List               ${list_akun}
    Press Keys             NONE            ESCAPE

    [Return]               ${list_akun}

Scrap Account
    [Arguments]         ${list_element}
    
    ${nameLength}       Get Length        ${list_element} 
    @{temp_list}        Create List

    FOR     ${j}        IN RANGE     0    ${nameLength}
        ${tempValue}            Get Text               ${list_element}[${j}]
        Append To List          ${temp_list}           ${tempValue} 
    END
    
    [Teardown]          Empty List Keyword
    [Return]            ${tempList}

Empty List Keyword
    @{temp_list}        Create List 
    [Return]            ${tempList}   

Scroll Menu
    [Arguments]     ${jumlah_scroll}
    FOR   ${i}   IN RANGE    0    ${jumlah_scroll}
        Click Element At Coordinates        //*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div        290        320
    END

Scroll Menu Up
    [Arguments]     ${jumlah_scroll}
    FOR   ${i}   IN RANGE    0    ${jumlah_scroll}
        Click Element At Coordinates        //*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div        290        -320
    END

Scraping Reply
    @{list_akun}                         Create List
    @{list_text}                         Create List

    FOR  ${i}  IN   @{list_thread}
        Go To                               ${i}
        Sleep                               10
        ${status}           Run keyword and Return Status     Wait Until Element Is Visible        //a[@href='/login']        10
        Run Keyword If     '${status}'=='True'    Reload Page
        Wait Until Element Is Visible       //article[@role="article"]            20
        ${temp_akun}        ${temp_text}        Scrap All Replies
        Append To List      ${list_akun}        ${tempAkun}
        Append To List      ${list_text}        ${tempText}
    END

    Replies To Excel    ${list_target}      ${list_akun}        ${list_text}

Scrap All Replies

    @{list_akun}        Create List
    @{list_text}        Create List
    
    FOR     ${j}        IN RANGE    1       1001
        ${article}         Set Variable           //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[contains(@style, 'linear')]/div/div/article/div/div/div/div[2]/div[2]
        ${acc_element}     Get WebElements        ${article}/div[1]/div/div/div[1]/div[1]/div/div[2]//span[contains(text(),"@")]
        # ${text_element}    Get WebElements        ${article}/div[2]
        
        ${article1}         Set Variable           //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div/article
        ${text_element}     Get WebElements        ${article1}
        ${tempAkun}        ${tempText}            Scrap Account Reply          ${acc_element}     ${text_element} 
        Append To List     ${list_akun}           ${tempAkun}
        Append To List     ${list_text}           ${tempText}
        ${status}          Run Keyword And Return Status    Wait Until Element Is Visible     //span[contains(text(),"Tampilkan balasan lainnya")]
        Run Keyword If    '${status}'=='True'     Scroll Element Into View     //span[contains(text(),"Tampilkan balasan lainnya")]
        Run Keyword If    '${status}'=='True'     Click Element     //span[contains(text(),"Tampilkan balasan lainnya")]
        Run Keyword If    '${status}'=='False'    Execute JavaScript         window.scrollBy(900, 1200);
        ${status}          Run Keyword And Return Status    Wait Until Element Is Visible     ${article1}//div[@role='button']//span[contains(text(),"Tampilkan")]
        Run Keyword If    '${status}'=='True'     Scroll Element Into View                  ${article1}//div[@role='button']//span[contains(text(),"Tampilkan")]
        Run Keyword If    '${status}'=='True'     Click Element                             ${article1}//div[@role='button']//span[contains(text(),"Tampilkan")]
        Sleep              1.5
        
    END
    
    Log List               ${list_akun}
    [Return]               ${list_akun}        ${list_text}

Scrap Account Reply
    [Arguments]         ${acc_element}    ${text_element}
    
    ${nameLength}       Get Length        ${text_element}
    @{temp_akun}        Create List
    @{temp_text}        Create List

    FOR     ${j}        IN RANGE     0    ${nameLength}
        # ${tempValue}            Get Text               ${acc_element}[${j}]
        # Append To List          ${temp_akun}           ${tempValue} 
        ${tempValue}            Get Text               ${text_element}[${j}]
        ${tempValue}            Format Reply           ${tempValue}
        # Append To List          ${temp_text}           ${tempValue}
        Append To List          ${temp_akun}           ${tempValue}[0] 
        Append To List          ${temp_text}           ${tempValue}[1] 
    END
    
    [Teardown]          Empty List Keyword
    [Return]            ${temp_akun}         ${temp_text}
