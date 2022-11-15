## OBO Role: NOR Manager

The NOR Manager has these basic duties:

1. Receiving `new ontology` requests on OBO and acknowledging the receipt
2. Including the ontology into the OBO NOR Dashboard
3. Supporting the NOR requestor to passing the OBO Dashboard
4. Assigning a provisional reviewer from the OBO Operations Committee
5. Removing the accepted ontology from the Dashboard upon acceptance


### Receiving `new ontology` requests on OBO and acknowledging the receipt

- The NOR Manager MUST actively listen to issues on the [OBO Issue Tracker](https://github.com/OBOFoundry/OBOFoundry.github.io/issues).
- When a new ontology request is received, and the wrong issue template was used, the NOR Manager must inform the NOR requestor to use the correct issue template and close the wrongly submitted issue.
- When a valid NOR request is received the NOR Manager acknowledges the receipt with the following message:
    ```markdown
    Dear @GITHUBNAME,
    
    Thank you for your submission. The review will be executed as a two stage process. 
    First, you will have to pass [OBO NOR Dashboard](https://obofoundry.org/obo-nor.github.io/dashboard/index.html). Pass means that no check _apart from `Users` may be red_.
    After you have successfully passed the Dashboard you will be assigned an OBO Operations committee member to review the ontology.
    
    Usually, the review will result in an opportunity to you to improve the ontology.
    When the reviewer believes the ontology is ready for presentation to the OBO Operations Committee, they will present
    your ontology during an OBO Operations Call. This gives other members of the
    committee the opportunity to assess your work.
    
    When a decision is reached by the committee you will be informed here on the issue tracker.
    The process can take any number of weeks or months, depending on the case at hand.
    Please inform us about any reasons you might have for increased urgency.
    
    You will be informed once your ontology is loaded in the OBO NOR Dashboard.
    
    Good luck.
    ```

### Including the ontology into the OBO NOR Dashboard


    After the dashboard is run, the OBO dashboard administrator informs the submitter about the need to fix the issues revealed by the dashboard, noting this is not part of the review itself, just a precursor, and that upon completion, a liaison will be assigned.
    At the next OBO Foundry Operations Committee conference call (hereafter, "Operations call"), a liaison is selected to be responsible for the issue. This liaison becomes familiar with the new ontology and rallies the appropriate people to provide feedback.
    At the next Operations call after that one, the liaison presents the NOR to the OBO Foundry Operations Committee and answers questions. In most cases, the information provided will be sufficient to either grant or refuse the prefix request. In some cases, the committee may choose to postpone its decision to require some clarification and fixes from the submitter. The liaison MUST be present at the Operations call in order for the NOR case to be discussed. If the liaison does not participate for 2 consecutive Operations calls, the chair of the second call emails the liaison to request a statement confirming the ability to continue as liaison. If the liaison does not participate in 3 consecutive Operations calls and did not respond to the email above, a new liaison is assigned during that third call.
