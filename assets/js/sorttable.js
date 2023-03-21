/*
 *   This content is licensed according to the W3C Software License at
 *   https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document
 *
 *   File:   sortable-table.js
 *
 *   Desc:   Adds sorting to a HTML data table that implements ARIA Authoring Practices
 *   Docs: https://w3c.github.io/aria-practices/examples/table/sortable-table.html
 */


'use strict';
class SortableTable {
  /**
   * initialize sortable table. Add button in table header to use for initializing sortable column
   * @param {Element} tableNode dom table element
   */
  constructor(tableNode) {
    this.tableNode = tableNode;
    this.selector = '.sort-button'

    //get all table headers
    this.columnHeaders = tableNode.querySelectorAll('thead th');

    this.sortColumns = [];

    //select table headers containing button element for sorting.
    for (var i = 0; i < this.columnHeaders.length; i++) {
      var ch = this.columnHeaders[i];
      var buttonNode = ch.querySelector(this.selector);
      if (buttonNode) {
        this.sortColumns.push(i);
        //set custom attribute for tracking sortable columns column-index.
        buttonNode.setAttribute('data-column-index', i);
        // handle button click event on table column
        buttonNode.addEventListener('click', this.handleClick.bind(this));
      }
    }

    this.optionCheckbox = document.querySelector(
      'input[type="checkbox"][value="show-unsorted-icon"]'
    );

    if (this.optionCheckbox) {
      this.optionCheckbox.addEventListener(
        'change',
        this.handleOptionChange.bind(this)
      );
      if (this.optionCheckbox.checked) {
        this.tableNode.classList.add('show-unsorted-icon');
      }
    }
  }

  /**
   * Takes the index of the column to be sorted parses sort parameters from html
   * @param {string|number} columnIndex
   */
  setColumnHeaderSort(columnIndex, chevron) {
    if (typeof columnIndex === 'string') {
      columnIndex = parseInt(columnIndex);
    }

    for (var i = 0; i < this.columnHeaders.length; i++) {
      var ch = this.columnHeaders[i];
      var buttonNode = ch.querySelector(this.selector);
      if (i === columnIndex) {
        //get the sort order from aria-sort attribute
        var value = ch.getAttribute('aria-sort');
        if (value === 'descending') {
          //change sort order parameter
          ch.setAttribute('aria-sort', 'ascending');
          //sort column
          this.sortColumn(
            columnIndex,
            'ascending',
            ch.classList.contains('num')
          );
          // Point chevron in appropriate direction
          chevron.setAttribute('class', 'bi-chevron-up')
        } else {
          //change sort order parameter
          ch.setAttribute('aria-sort', 'descending');
          //sort column
          this.sortColumn(
            columnIndex,
            'descending',
            ch.classList.contains('num')
          );
          // Point chevron in appropriate direction
          chevron.setAttribute('class', 'bi-chevron-down')
        }
      } else {
        if (ch.hasAttribute('aria-sort') && buttonNode) {
          ch.removeAttribute('aria-sort');
        }
      }
    }
  }

  /**
   * Sort table column data given the below parameters
   * @param {number} columnIndex
   * @param {string} sortValue sort order
   * @param {boolean} isNumber
   */
  sortColumn(columnIndex, sortValue, isNumber) {
    function compareValues(a, b) {
      if (sortValue === 'ascending') {
        if (a.value === b.value) {
          return 0;
        } else {
          if (isNumber) {
            return a.value - b.value;
          } else {
            return a.value < b.value ? -1 : 1;
          }
        }
      } else {
        if (a.value === b.value) {
          return 0;
        } else {
          if (isNumber) {
            return b.value - a.value;
          } else {
            return a.value > b.value ? -1 : 1;
          }
        }
      }
    }

    if (typeof isNumber !== 'boolean') {
      isNumber = false;
    }

    var tbodyNode = this.tableNode.querySelector('tbody');
    var rowNodes = [];
    var dataCells = [];

    var rowNode = tbodyNode.firstElementChild;

    var index = 0;
    //extract table data cells
    while (rowNode) {
      rowNodes.push(rowNode);
      var rowCells = rowNode.querySelectorAll('th, td');
      var dataCell = rowCells[columnIndex];

      var data = {};
      data.index = index;
      data.value = dataCell.textContent.toLowerCase().trim();
      if (isNumber) {
        data.value = parseFloat(data.value);
      }
      dataCells.push(data);
      rowNode = rowNode.nextElementSibling;
      index += 1;
    }
    // sort extracted data cells
    dataCells.sort(compareValues);

    // remove rows
    while (tbodyNode.firstChild) {
      tbodyNode.removeChild(tbodyNode.lastChild);
    }

    // add sorted rows
    for (var i = 0; i < dataCells.length; i += 1) {
      tbodyNode.appendChild(rowNodes[dataCells[i].index]);
    }
  }

  /* EVENT HANDLERS */

  handleClick(event) {
    var tgt = event.currentTarget;
    //get the column to sort and pass index t
    this.setColumnHeaderSort(
      tgt.getAttribute('data-column-index'),
      tgt.firstElementChild
    );
  }

  handleOptionChange(event) {
    var tgt = event.currentTarget;

    if (tgt.checked) {
      this.tableNode.classList.add('show-unsorted-icon');
    } else {
      this.tableNode.classList.remove('show-unsorted-icon');
    }
  }
}