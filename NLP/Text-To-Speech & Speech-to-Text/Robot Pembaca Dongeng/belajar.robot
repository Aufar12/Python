*** Settings ***
Documentation   Belajar Aja
Library         SeleniumLibrary
Library         Collections
Library         scrapToSpeech.py

*** Variables ***
${Keyword}      Sangkuriang
${url}          http://dongeng.org
${url1}         http://dongeng.org/?s=${Keyword} 
${browser}      Chrome

# Test Cases / Tasks 
*** Tasks *** 
Day 9  
    kosonginSheet
    Open Browser    ${url}          ${browser}
    Buka Google
    ${dongeng}      Scrap
    Close Browser
    prosesDongeng   ${Keyword}      ${dongeng}
    Log to Console      Loading Baca Dongeng...
    bacaDongeng

    
*** Keywords ***
Buka Google
    Go To        ${url1}

    ${x}=      Set Variable             xpath=//*[@id="page"]//h2

    Wait Until Element Is Visible       ${x}      60
    Click Element                       ${x}

Scrap

    ${x}        Set Variable        xpath=//article/div[1]/div/div[1]
    
    Wait Until Element Is Visible       ${x}      60

    ${jumlah}=      Get Element Count       ${x}/p
    ${judul}=       Get Text                xpath=//h1
    ${penulis}=     Get Text                xpath=//header/div/span[1]
    ${waktu}=       Get Text                xpath=//header/div/span[2]

    ${temp}=      Create List   
    
    FOR    ${i}    IN RANGE    0    ${jumlah}
        ${paragraf}=   Get Text       ${x}/p[${i+1}]
        Append To List    ${temp}    ${paragraf}
    END

    ${semua}=      Create List
    Append To List    ${semua}    ${judul}
    Append To List    ${semua}    ${penulis}
    Append To List    ${semua}    ${waktu}
    Append To List    ${semua}    ${temp}
    Log to Console      ${semua}

    [return]        ${semua}




# Referensi
# Keywords : https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
# Run Keyword If      ${jumlah} < 2       Baca Dengan Iklan
# ${x}=      Set Variable      "SSSS"
# Exit For Loop If      ${x} == 10

# Error
# The result of the xpath expression "/" is: [object HTMLDocument]. It should be an element.