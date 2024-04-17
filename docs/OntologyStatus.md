---
layout: doc
title: Ontology status
---

Info: this page is non-normative; definitions may change.

An ontology can be active, inactive, unresponsive, orphaned or obsolete

These statuses depend on "Maintenance" (defined in [Principle 16](https://obofoundry.org/principles/fp-016-maintenance.html
)) and "Responsiveness" ([Principle 20](https://obofoundry.org/principles/fp-016-maintenance.html)).

The table below shows the statuses with their corresponding values for "Responsive" and "Maintained".

<table class="tg">
  <tbody>
    <tr>
      <th class="tg-lbaf" align="left">&nbsp;Status&nbsp;</th>
      <th class="tg-lbaf" align="center">&nbsp;Responsive&nbsp;</th>
      <th class="tg-lbaf" align="center">&nbsp;&nbsp;Maintained&nbsp;&nbsp;</th>
    </tr>
    <tr>
      <td align="left">&nbsp;Active&nbsp;</td>
      <td align="center">&nbsp;yes&nbsp;</td>
      <td align="center">&nbsp;&nbsp;yes&nbsp;&nbsp;</td>
    </tr>
    <tr>
      <td align="left">&nbsp;Inactive&nbsp;</td>
      <td align="center">&nbsp;yes&nbsp;</td>
      <td align="center">&nbsp;&nbsp;no&nbsp;&nbsp;</td>
    </tr>
    <tr>
      <td align="left">&nbsp;Unresponsive&nbsp;</td>
      <td align="center">&nbsp;no&nbsp;</td>
      <td align="center">&nbsp;&nbsp;yes&nbsp;&nbsp;</td>
    </tr>
    <tr>
      <td align="left">&nbsp;Orphaned&nbsp;</td>
      <td align="center">&nbsp;no&nbsp;</td>
      <td align="center">&nbsp;&nbsp;no&nbsp;&nbsp;</td>
    </tr>
    <tr>
      <td align="left">&nbsp;Obsolete&nbsp;</td>
      <td align="center">&nbsp;(yes/no)&nbsp;</td>
      <td align="center">&nbsp;&nbsp;no&nbsp;&nbsp;</td>
    </tr>
  </tbody>
</table>
<br>

- _active_: The ontology project has a contact person who is responsive. Terms, with resolvable IRIs, are being added (if the ontology is growing and not deemed complete) or other revisions made in response to community requests and/or the aims of the editorial team.
- _inactive_: The ontology project has a contact person who is responsive. A version of the ontology is available, but no edits are being made and requests for edits are either greatly delayed or not being addressed by the ontology's editors.
- _unresponsive_: The ontology project does not have a contact person who is responsive, but the ontology is still being actively maintained.
- _orphaned_: The ontology project does not have a contact person who is responsive. A static version of the ontology exists, but no edits are being made and requests for edits are not being addressed or responded to by the ontology's editors.
- _obsolete_: The ontology is not maintained (inactive or orphaned), and the original developers do not recommend using existing versions of it, either because another project is available that supersedes it, or because previous produced versions have serious issues that make them less usable, and/or are not available at all. Note that "Obsolete" is a special status--designated by the _ontology representative_ rather than by the OBO Foundry--that acts as confirmation that the ontology is deprecated.

Please refer to the OBOFoundry GitHub [issue](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1126) and [other issue about "unresponsive"](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2255) for discussions on the subject.
