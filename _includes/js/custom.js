jQuery(document).ready(function() {

    function search() {
        $('#close', search).hide();
        var data = false;
        var matches = false;
        var search = $('#search');
        var find = function(phrase) {
            if (!data) {
                return $.ajax({
                    url: '/search.json',
                    dataType: 'json',
                    success: function(resp) {
                        data = _(resp).chain()
                            .compact()
                            .map(function(p) {
                                p.words = (p.title.toLowerCase() + ' ' + p.summary.toLowerCase()).match(/(\w+)/g);
                                return p;
                            })
                            .value();
                        find(phrase);
                    }
                });
            }

            matches = _(data).filter(function(p) {
                return _(phrase).filter(function(a) {
                    return _(p.words).any(function(b) {
                        return a === b || b.indexOf(a) === 0;
                    });
                }).length === phrase.length;
            });

            $(matches).each(function() {
                $('#search-results', search).append('<li><h6>' + this.title + '</h6><p>' + this.title + '... <small><a href="' + this.url + '">Read more</a></small></p><hr></li>');
            });

            $('#search-results', search).show();
            $('#close', search).show();
        };
        $('input', search).bind("focus", _(function() {
            $('#search-results', search).empty();
            $('#search-results', search).hide();
            $('#close', search).hide();

            var phrase = $('input', search).val();
            if (phrase.length >= 4) {
                find(phrase.toLowerCase().match(/(\w+)/g));
            }
            return false;
        }).debounce(100));

        $('#close', search).bind("click", function() {
            $('#search-results', search).hide();
            $('#close', search).hide();
            return false;
        });

        $('input', search).keyup(_(function() {
            $('#search-results', search).empty();
            $('#search-results', search).hide();
            $('#close', search).hide();

            var phrase = $('input', search).val();
            if (phrase.length >= 4) {
                find(phrase.toLowerCase().match(/(\w+)/g));
            }
            return false;
        }).debounce(100));
    };
    search();
    //set the first character os string to uppercase
    function capitalize(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }
    //surround data table rows generated in rendertable function with table head
    function tableHtml(content, domain = false, tableDomains) {
        return `<div><strong>${ domain? capitalize(tableDomains): ""}</strong></div>
                <table id="ont_table" class="table table-hover sortable">
                    <thead>
                        <tr class="row">
                            <th scope="col" class="col-sm-1 ob-center">
                                <span>ID</span>
                                <button type="button" class="btn btn-outline-default btn-xs" title="Sort by ID" data-sort="id" >
                                    <span aria-hidden="true" class="glyphicon glyphicon-chevron-down"></span>
                                </button>
                            </th>
                            <th scope="col" class="col-sm-1 ob-center">
                                <span>Title</span>
                                <button type="button" class="btn btn-outline-default btn-xs" title="Sort by title" data-sort="title" >
                                    <span aria-hidden="true" class="glyphicon glyphicon-chevron-down"></span>
                                </button>
                            </th>
                            <th scope="col" class="col-sm-3 ob-center">
                                <span>Description</span>
                            </th>
                            <th scope="col" class="col-sm-4 ob-center">
                                <span>Quick Access</span>
                            </th>
                            <th scope="col" class="col-sm-2 ob-center">
                                <span>Re-Use</span>
                                <button type="button" class="btn btn-outline-default btn-xs" title="Sort by License" data-sort="license" >
                                    <span aria-hidden="true" class="glyphicon glyphicon-chevron-down"></span>
                                </button>
                            </th>
                            <th scope="col" class="col-sm-1 ob-center">
                                <span>Social</span>
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        ${content}
                    </tbody>
                </table>
                `;
    }

    /**
     * converts json data passed in into renderTable into html table
     * @param {object} data Ontology json data.
     * @param {boolean} [domain=false]
     */
    function renderTable(data, domain= false ) {
        let table = ``;
        let domainTables = ``;
        let tableDomains = []; // list of domains
        let tableDomainhtml = {}; // hold html table data with domain as key
        for (let i = 0; i < data.length; i++) {
            let id = data[i]['id'];
            let is_obsolete = "";
            let is_inactive = "";
            let activity_status = data[i]['activity_status']
            let title = data[i]['title'];
            let license_url = "#";
            let license_logo = "#";
            let license_label = "";
            let description = data[i]['description'];
            let repo = "";
            let homepage = data[i]["homepage"];
            let tracker = "";
            let contact = "";
            let publication = "";
            let domainInner = ["Unknown"];

            if (data[i]['license']) {
                license_url = data[i]["license"]["url"];
                license_logo = data[i]["license"]["logo"];
                license_label = data[i]["license"]["label"];
            }
            if (data[i]["repository"] && data[i]["repository"].includes("https://github.com/")) {
                repo = data[i]["repository"];
            }
            if (data[i]["tracker"]) {
                tracker =`<a class="btn btn-default" href="${data[i]["tracker"]}" aria-label="Go to the tracker for ${title}" title="Go to the tracker for ${title}">
                                <span class="glyphicon glyphicon-comment" aria-hidden="true"></span>
                            </a>`;
            } else {
                tracker = `
                        <a class="btn btn-default disabled">
                            <span class="glyphicon glyphicon-comment" aria-hidden="true"></span>
                        </a>`;
            }
            if (data[i].hasOwnProperty("domain") && data[i]['domain'] !== undefined) {
                domainInner[0] = data[i]['domain'];
            }
            if (description !== undefined && description.toString().length > 140) {
                description = description.toString().slice(0, 140).trim() + '...'
            }
            if (data[i]["contact"]) {
                contact =`
                        <a class="btn btn-default btn-sm" href="mailto:${data[i]["contact"]["email"]}" aria-label="Send an email to ${title}"
                           title="Send an email to ${title}">\
                            <span class="glyphicon glyphicon-envelope" aria-hidden="true"></span>
                        </a>`;
            }
            if (data[i]["publications"] && data[i]["publications"].length > 0) {
                publication = `
                            <a class="btn btn-default btn-sm" href="${data[i]["publications"][0]["id"]}" aria-label="View the primary publication for ${title}" title="View the primary publication for ${title}">
                                <span class="glyphicon glyphicon-book" aria-hidden="true"></span>
                            </a>`;
            }
            if (activity_status === "inactive") {
                is_inactive = "inactive_row";
            }
            if (data[i]["is_obsolete"]) {
                is_obsolete = "(obsolete)"
            }
            // table row template
            let template = `
                <tr class="row ${is_inactive}">
                        <a class="" href="ontology/${id}.html">
                           ${id} 
                    <th scope="row" class="col-sm-1">
                        </a>
                        <span style="background-color: #ff8d82">${is_obsolete}</span>    
                    </td>
                    <td class="col-sm-1">
                        ${title}
                    </td>
                    <td class="col-sm-3">
                        ${description}
                        <small>
                            <a href="ontology/${id}.html">Detail</a>
                        </small>
                    </td>
                    <td class="col-sm-5">
                        <div class="btn-group btn-group-sm" role="group">
                            <a role="button" class="btn btn-default" href="ontology/${id}.html" aria-label="More details for ${title}" title="More details for ${title}">
                                  <span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span>
                            </a>
                            <a role="button" class="btn btn-default" href="${homepage}" aria-label="Go to the homepage for ${title}" title="Go to the homepage for ${title}">
                                 <span class="glyphicon glyphicon-home" aria-hidden="true"></span>
                            </a>
                            <a role="button" class="btn btn-default" href="http://purl.obolibrary.org/obo/${id}.owl" aria-label="Download ${title} in OWL format" title="Download ${title} in OWL format">
                                <span class="glyphicon glyphicon-download" aria-hidden="true"></span>
                            </a>
                            <a role="button" class="btn btn-default" href="http://www.ontobee.org/browser/index.php?o=${id}" aria-label="Browse ${title} on OntoBee" title="Browse ${title} on OntoBee">
                                <span class="glyphicon glyphicon-eye-open" aria-hidden="true"></span>
                            </a>
                            ${tracker}
                            ${contact}
                            ${publication}
                        </div>
                    </td>
                    <td class="col-sm-1">
                        <a href="${license_url}" >
                            <img width="100px" src="${license_logo}" alt="${license_label}"/><br>
                            <span style="display: none">${license_label}</span>
                        </a>
                    </td>  
                    <td class="col-sm-1">
                        <a href="${repo}">
                            <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/${repo.replace("https://github.com/", "")}?style=social" />
                        </a>
                    </td>
                                    
                </tr>
            `;


            if (domain === true) {
                tableDomains.push(domainInner[0].trim())
                if (!tableDomainhtml.hasOwnProperty(domainInner[0].trim())) {
                    tableDomainhtml[domainInner[0].trim()] = template;
                } else {
                    tableDomainhtml[domainInner[0].trim()] += template;
                }
            }
            table += template;
        }
        if (domain === true) {
            tableDomains = [...new Set(tableDomains)]
            //loops through list of domains and surrounds html row with table tag and headers
            for (let i = 0; i < tableDomains.length; i++) {
                let content = tableDomainhtml[tableDomains[i]];

                let table = tableHtml(content, true, tableDomains[i]);

                // merge all final table html generated above with the upper domain at top.
                if (tableDomains[i].toLowerCase() === "upper") {
                    domainTables = table + domainTables;
                } else {
                    domainTables = domainTables + table;
                }

            }
        }
        // append table(s) generated depending on if domain filter is active or not.
        if (domain === true) {
            $("#tableDiv").html(domainTables);
        } else {
            let res = tableHtml(table, false, "")
            $("#tableDiv").html(res);
        }
    }

    /**
     * Sort json ontology data by the given sort field
     * @param {Object} data
     * @param {string|number} sortField
     */
    function sortByField(data, sortField) {
        return data.sort(function(a, b) {
            if (a[sortField] === undefined || b[sortField] === undefined) {
                return 0;
            }
            if (a[sortField].toLowerCase() < b[sortField].toLowerCase()) {
                return -1;
            }
            if (a[sortField].toLowerCase() > b[sortField].toLowerCase()) {
                return 1;
            }
            return 0;
        });
    }

    /**
     * make a function wait for a given amount of time before running
     * @param {*} func
     * @param {number} timeout
     */
    function debounce(func, timeout = 300) {
        let timer;
        return (...args) => {
            clearTimeout(timer);
            timer = setTimeout(() => {
                func.apply(this, args);
            }, timeout);
        };
    }

    /**
     * applies selected checkbox filter to data passed in
     * @param {object} data
     */
    function applyFilters(data) {
        let selector = $("[data-filter]");
        let domain = selector[0].checked
        let hideactive = selector[1].checked
        let hideObsolete = selector[2].checked
        let filteredData = [];

        if (!domain && !hideactive && !hideObsolete) {
            renderTable(data);
        } else if (domain && !hideactive && !hideObsolete) {
            renderTable(sortByField(data, "domain"), true);
        } else if (domain && hideactive && !hideObsolete) {
            filteredData = data.filter(x => x["activity_status"] === "active");
            renderTable(sortByField(filteredData, "domain"), true);
        } else if (domain && !hideactive && hideObsolete) {
            filteredData = data.filter(x => x["is_obsolete"] !== true);
            renderTable(sortByField(filteredData, "domain"), true);
        } else if (domain && hideactive && hideObsolete) {
            filteredData = data.filter(x => x["is_obsolete"] !== true)
                .filter(x => x["activity_status"] === "active");
            renderTable(sortByField(filteredData, "domain"), true);
        } else if (!domain && hideactive && hideObsolete) {
            filteredData = data.filter(x => x["is_obsolete"] !== true)
                .filter(x => x["activity_status"] === "active");
            renderTable(filteredData);
        } else if (!domain && hideactive && !hideObsolete) {
            filteredData = data["ontologies"].filter(x => x["activity_status"] === "active");
            renderTable(filteredData);
        } else if (!domain && !hideactive && hideObsolete) {
            filteredData = data.filter(x => x["is_obsolete"] !== true);
            renderTable(filteredData);
        }
    }

    /**
     * Search the given fields {domain, description, id} for input text
     * @param {*} input input is a Jquery selector of the search box
     * @param {object} JsonData Ontology data to search through
     * @return {object} returns filtered json data
     */
    function Search(input, JsonData) {
        let value = input.val().toLowerCase();
        // check text length greater than 2 before doing search
        if (value.length >= 2) {
            return JsonData.filter((row) => {
                let term = input.val().toLowerCase();
                if (row.domain === undefined) {
                    row.domain = ""
                }
                if (row.description === undefined) {
                    row.description = ""
                }
                if (row.title === undefined) {
                    row.title = ""
                }
                return (row.id.toLowerCase().includes(term) ||
                    row.domain.toLowerCase().includes(term) ||
                    row.title.toLowerCase().includes(term) ||
                    row.description.toLowerCase().includes(term))
            });
        }
        return JsonData;
    }

    /**
     * applies filters taking into consideration the state of
     * all the other filters and search text
     * @param {object} data
     */
    function apply_all_filters(data) {
        let selectedDomain = $("#dd-domains").children("option:selected").val();
        let res = data["ontologies"].filter(x => x["domain"] !== undefined);
        let dt = res.filter(x => x["domain"].includes(selectedDomain));
        let dt2 = Search($("#searchVal"), dt);
        applyFilters(dt2)
    }
// obtain json data using fetch
    fetch('/registry/ontologies.jsonld')
        .then(response => response.json())
        .then((data) => {

            // create change observer to handle sorting when we have single and multiple tables based on domains
            let target = document.querySelector('#tableDiv')
            // Create an observer instance.
            let observer = new MutationObserver(function(mutations) {
                let sortableTables = document.querySelectorAll('table.sortable');
                for (let i = 0; i < sortableTables.length; i++) {
                    new SortableTable(sortableTables[i]);
                }
            });
            // Pass in the target node, as well as the observer options.
            observer.observe(target, {
                attributes: true,
                childList: true,
                characterData: true
            });

            // extract domain and set values for dropdown menu
            let domains = [];
            for (let k = 0; k < data["ontologies"].length; k++) {
                if (data["ontologies"][k]["domain"] !== undefined) {
                    let d = data["ontologies"][k]["domain"] //.replace(" and", ",").split(",")
                    domains.push(d)
                }
            }
            domains = [...new Set(domains)];
            domains.sort();
            $("#dd-domains").append(`<option></option>`);
            domains.forEach(function(r) {
                $("#dd-domains").append(`<option value="${r.trim()}">${r.trim()}</option>`);
            })
            //render table on page load
            renderTable(data["ontologies"]);

            // check box filter event for table data
            $("[data-filter]").on("change", () => {
                apply_all_filters(data)
            });
            // get table by domain dropdown
            $("#dd-domains").on("change", () => {
                apply_all_filters(data)

            });
            // search word in table
            $("#searchVal").on("keyup", debounce((e) => {
                apply_all_filters(data)
            }));

            // dispatch change event on initial load to apply checkbox filters
            let element = document.querySelector('[data-filter]');
            let event = new Event('change');
            element.dispatchEvent(event);
            $('#table-main').css('display', 'block');
            $( 'a' ).tooltip({
                tooltipClass: "mytooltipstyle",
                show: {
                    effect: "slideDown",
                }
            });
        }).catch(error => console.log(error));
});