*** Settings ***
Library             SeleniumLibrary    run_on_failure=Nothing
Library             Process
Library             OperatingSystem
Library             Collections
Library             String
Library		        customModules.py

*** Variables ***
${URL}                   https://www.senheng.com.my/home-entertainment/tv.html
${BROWSER}               Chrome
${total_scrap_data}      1000
${folder_image}          ${CURDIR}/image_result
${product_div}           //div[@class="row product-container"]//div[@class="content"]/div
${title_path}            //*[@id="maincontent"]//h1
${price_path}            //*[@id="maincontent"]/div[4]/div[2]/div[1]/span[2]
${first_image_path}      //div[@class="productSlider__thumbnail--item"]//img 
${trade_in_path}         //button[contains(text(),"Yes (-RM")]  
${promotions_path}       //a[contains(text(),"Available Voucher")]
${viewed_today_path}     //p[contains(text(),"Customers viewed today")]     
${short_desc_path}       //*[@id="maincontent"]//div[@class='short-description__text']
${spec_tab_path}         //span[contains(text(),"Specification")]
${spec_content_path}     //*[@id="full-width-tabpanel-1"]
${review_count_path}     //*[@id="maincontent"]/div[4]/div[2]/div[4]/p[1]
@{result_list}

*** Test Cases ***

Preparation
    Open Browser    ${URL}   ${BROWSER}
    Create Directory    ${folder_image}
    Maximize Browser Window
Test
    Go To    https://www.dhl.com/id-en/home/tracking/tracking-express.html
    #Sleep    10000000000
    Wait Until Element Is Visible    //button[@id="onetrust-reject-all-handler"]    timeout=10s
    Click Element    //button[@id="onetrust-reject-all-handler"]
    Input Text    //*[@id="c-tracking--input"]    5548230321
    Click Button    //button[@type="submit"]
    Sleep    100000000
    Execute Javascript    return document.evaluate('//*[@id="c-tracking--input"]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.value=5548230321;
    Execute Javascript    return document.evaluate('//button[@type="submit"]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();
    #Submit Form
    Sleep    10000000000
# Website Scraping
#     FOR     ${i}        IN RANGE     1      ${total_scrap_data}
#         Log To Console    Product No : ${i}

#         # Product Div
#         ${status}    ${value}    Run Keyword And Ignore Error    Wait Until Element Is Visible    ${product_div}/div[${i}]
#         Exit For Loop If    '${status}'=='FAIL'
#         Scroll Element Into View    ${product_div}/div[${i}]
#         Run Keyword and Ignore Error    Click and Get Text Element using Javascript     ${product_div}/div[${i}]//a    //p

#         # Title
#         Wait Until Element Is Visible    ${title_path}
#         ${title}    Get Text    ${title_path}

#         # Image
#         ${image_path}    Save Product Image    Product ${i} - ${title}

#         # Price
#         ${price}    Get Text    ${price_path}

#         # Trade-In
#         ${trade_in}    Check Available Promotions & Trade In    Trade In

#         # Promotions
#         ${promotions}    Check Available Promotions & Trade In    Promotions
        
#         # Viewed Today
#         ${viewed_today}    Get Text    ${viewed_today_path}
#         ${viewed_today}    Remove String and Convert to Integer    ${viewed_today}    Customers viewed today

#         # Short-Text
#         ${short_desc}    Get Text    ${short_desc_path}

#         # Specifications
#         ${spec_content}    Click and Get Text Element using Javascript    ${spec_tab_path}    ${spec_content_path}

#         # Reviews
#         ${review_count}    Get Text    ${review_count_path}
#         ${status}    ${value}    Run Keyword And Ignore Error    Remove String and Convert to Integer    ${review_count}    Review
#         ${review_count}    Set Variable If    '${status}' == 'PASS'    ${value}    0
        
#         # Store All Value to List
#         &{temp_dict}    Create Dictionary    Title=${title}    Image=${image_path}    Price=${price}    TradeIn=${trade_in}    
#         ...    Promotions=${promotions}    ViewedToday=${viewed_today}    ShortDesc=${short_desc}    Specification=${spec_content}    ReviewCount=${review_count}
#         Append To List    ${result_list}    ${temp_dict}
#         Log To Console    ${temp_dict}
#         Go Back
#     END
    
# Write to Excel and Build Graph
#     List Dict To Excel    ${result_list}

# *** Keywords ***
# Click and Get Text Element using Javascript
#     [Arguments]    ${element_click}    ${element_text}
#     Execute Javascript    return document.evaluate('${element_click}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();
#     Wait Until Element Is Visible    ${element_text}
#     ${result}    Get Text    ${element_text}
#     [Return]    ${result}

# Remove String and Convert to Integer
#     [Arguments]    ${input}    ${str_to_remove}
#     ${result}    Remove String    ${input}    ${str_to_remove}
#     ${result}    Convert To Integer    ${result}
#     [Return]    ${result}

# Save Product Image
#     [Arguments]    ${title}
#     # Using Capture Element Screenshot
#     Scroll Element Into View    ${first_image_path}
#     ${image_path}    Set Variable    ${folder_image}/${title}.jpg
#     Capture Element Screenshot    ${first_image_path}    ${image_path}

#     # Using Run Process
#     ${image_url}    Get Element Attribute    ${first_image_path}    src
#     Run Process  curl  -o  ${image_path}    ${image_url}

#     [Return]    ${image_path}    

# Check Available Promotions & Trade In
#     [Arguments]    ${input}
#     ${element}    Set Variable If    '${input}' == 'Trade In'    ${trade_in_path}    ${promotions_path}
#     ${status}    ${value}    Run Keyword And Ignore Error    Get Text    ${element}
#     ${value}    Set Variable If    '${status}' == 'PASS'    ${value}    - 
#     [Return]    ${value}
    