jQuery(document).ready(function () {

    function search() {
        $('#close', search).hide();
        var data = false;
        var matches = false;
        var search = $('#search');
        var find = function (phrase) {
            if (!data) {
                return $.ajax({
                    url: '/search.json',
                    dataType: 'json',
                    success: function (resp) {
                        data = _(resp).chain()
                            .compact()
                            .map(function (p) {
                                p.words = (p.title.toLowerCase() + ' ' + p.summary.toLowerCase()).match(/(\w+)/g);
                                return p;
                            })
                            .value();
                        find(phrase);
                    }
                });
            }

            matches = _(data).filter(function (p) {
                return _(phrase).filter(function (a) {
                    return _(p.words).any(function (b) {
                        return a === b || b.indexOf(a) === 0;
                    });
                }).length === phrase.length;
            });

            $(matches).each(function () {
                $('#search-results', search).append('<li><h6>' + this.title + '</h6><p>' + this.title + '... <small><a href="' + this.url + '">Read more</a></small></p><hr></li>');
            });

            $('#search-results', search).show();
            $('#close', search).show();
        };
        $('input', search).bind("focus", _(function () {
            $('#search-results', search).empty();
            $('#search-results', search).hide();
            $('#close', search).hide();

            var phrase = $('input', search).val();
            if (phrase.length >= 4) {
                find(phrase.toLowerCase().match(/(\w+)/g));
            }
            return false;
        }).debounce(100));

        $('#close', search).bind("click", function () {
            $('#search-results', search).hide();
            $('#close', search).hide();
            return false;
        });

        $('input', search).keyup(_(function () {
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

    function capitalize(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    }
    //surround data table rows generated in rendertable function with table head
    function tableHtml(content, domain=false, tableDomains){
         return`<div><strong>${ domain? capitalize(tableDomains): ""}</strong></div>
                            <table id="ont_table" class="table table-hover sortable">
                                 <thead>
                                 <tr class="row">
                                  <th class="col-sm-1" >ID
                                   <button type="button" class="btn btn-outline-default btn-sm" title="Sort by ID" data-sort="id" style="float: right">
                                    <span aria-hidden="true" class="glyphicon glyphicon-chevron-down"></span>
                                  </button>
                                  </th>
                                  <th class="col-sm-1" >Title
                                    <button type="button" class="btn btn-outline-default btn-sm" title="Sort by title" data-sort="title" style="float: right">
                                        <span aria-hidden="true" class="glyphicon glyphicon-chevron-down"></span>
                                    </button>
                                 </th>
                                  <th class="col-sm-3">Description</th>
                                  <th class="col-sm-4">Quick Access</th>
                                  <th class="col-sm-2" >Re-Use
                                       <button type="button" class="btn btn-outline-default btn-sm" title="Sort by License" data-sort="license" style="float: right">
                                        <span aria-hidden="true" class="glyphicon glyphicon-chevron-down"></span>
                                      </button>
                                    </th>
                                  <th class="col-sm-1">Social</th>
                                 </tr>
                                
                                 </thead>
                                 <tbody>${content}</tbody>
                            </table>
                `;
    }

    function renderTable(data, domain="") {
        let table = ``;
        let domainTables = ``;
        let tableDomains =[];
        let tableDomainhtml = {};
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
            let tracker = "#";
            let contact = "";
            let publication = "";
            let foundry_order = "";
            let domainInner = ["Unknown"];

            if (data[i]['license']) {
                license_url = data[i]["license"]["url"];
                license_logo = data[i]["license"]["logo"];
                license_label = data[i]["license"]["label"];
            }
            if (data[i]["repository"] && data[i]["repository"].includes("https://github.com/")){
                repo = data[i]["repository"];
            }
            if (data[i]["tracker"]) {
                tracker = data[i]["tracker"];
            }
            if(data[i].hasOwnProperty("domain") && data[i]['domain'] !== undefined){
                domainInner[0] = data[i]['domain'];
            }
            if(description !== undefined && description.toString().length > 140){
                description = description.toString().slice(0, 140) + '...'
            }
            if (data[i]["contact"]){
                contact = data[i]["contact"]["email"];
            }
            if (data[i]["publications"]   && data[i]["publications"].length > 0){
                console.log(data[i]["publications"], id)
                publication = data[i]["publications"][0]["id"];
            }
            if (data[i]["in_foundry_order"]) {
                foundry_order = `
                        <a class="col-sm-1 btn btn-default btn-sm" href="/principles/fp-000-summary.html" aria-label="Left Align">
                               <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
                        </a>             
                `;
            }
            if(activity_status === "inactive"){
                is_inactive ="inactive_row";
            }
            if(data[i]["is_obsolete"]){
                is_obsolete = "(obsolete)"
            }
            let template = `
                <tr class="row ${is_inactive}">
                    <td class="col-sm-1">
                        <a class="" href="ontology/${id}.html">
                           ${id} 
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
                        <div class="ic-display">
                            <a class="btn btn-default btn-sm" href="ontology/${id}.html" aria-label="Left Align" title="More details">
                                  <span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span>
                            </a>
                            <a class="btn btn-default btn-sm" href="${homepage}" aria-label="Left Align" title="Project home">
                                 <span class="glyphicon glyphicon-home" aria-hidden="true"></span>
                            </a>
                            <a class="btn btn-default btn-sm" href="${tracker}" aria-label="Left Align" title="Tracker">
                                <span class="glyphicon glyphicon-comment" aria-hidden="true"></span>
                            </a>
                            <a class="btn btn-default btn-sm" href="mailto:${contact}" aria-label="Left Align" title="Email ontology devs">\
                                <span class="glyphicon glyphicon-envelope" aria-hidden="true"></span>
                            </a>
                            <a class="btn btn-default btn-sm" href="http://purl.obolibrary.org/obo/${id}.owl" aria-label="Left Align" title="Download file">
                                <span class="glyphicon glyphicon-download" aria-hidden="true"></span>
                            </a>
                            <a class="btn btn-default btn-sm" href="http://www.ontobee.org/browser/index.php?o=${id}" aria-label="Left Align" title="Browse on Ontobee">
                                <span class="glyphicon glyphicon-eye-open" aria-hidden="true"></span>
                            </a>
                            <a class="btn btn-default btn-sm" href="${publication}" aria-label="Left Align" title="Publications list">
                                <span class="glyphicon glyphicon-book" aria-hidden="true"></span>
                            </a>
                            ${foundry_order}
                        </div>
                    </td>
                    <td class="col-sm-1">
                        <a href="${license_url}" >
                            <img width="100px" src="${license_logo}" alt="${license_label}"/>
                        </a>
                    </td>  
                    <td class="col-sm-1">
                        <a href="${repo}">
                            <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/${repo.replace("https://github.com/", "")}?style=social" />
                        </a>
                    </td>
                                    
                </tr>
            `;


            if( domain !== ""){
                    tableDomains.push(domainInner[0].trim())
                    if(!tableDomainhtml.hasOwnProperty(domainInner[0].trim())){
                        tableDomainhtml[domainInner[0].trim()] = template;
                    }else{
                        tableDomainhtml[domainInner[0].trim()] += template;
                    }
            }
            table += template;
        }
        if( domain !== ""){
            tableDomains = [...new Set(tableDomains)]
            for(let i=0; i<tableDomains.length; i++){
                let content = tableDomainhtml[tableDomains[i]];

                let table = tableHtml(content, true, tableDomains[i]);
                if(tableDomains[i].toLowerCase() === "upper"){
                    domainTables = table + domainTables;
                }else{
                    domainTables = domainTables + table;
                }

            }
        }

        if( domain !== ""){
            $("#tableDiv").html(domainTables);
        }else{
             let res = tableHtml(table, false, "")
            $("#tableDiv").html(res);
        }
    }

    function sortByField (data, sortField){
        return data.sort(function (a, b) {
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
    function debounce(func, timeout = 300){
      let timer;
      return (...args) => {
        clearTimeout(timer);
        timer = setTimeout(() => { func.apply(this, args); }, timeout);
      };
    }
    function applyFilters(data){
        let selector  = $("[data-filter]");
                let domain = selector[0].checked
                let hideactive = selector[1].checked
                let hideObsolete = selector[2].checked

                if(!domain && !hideactive && !hideObsolete){
                    renderTable(data);
                }else if(domain && !hideactive && !hideObsolete){
                    renderTable(sortByField(data, "domain"), "domain");
                }else if(domain && hideactive && !hideObsolete){
                    let filteredData = data.filter(x => x["activity_status"] === "active");
                    renderTable(sortByField(filteredData, "domain"), "domain");
                }else if(domain && !hideactive && hideObsolete){
                    let filteredData = data.filter(x => x["is_obsolete"] !== true);
                    renderTable(sortByField(filteredData, "domain"), "domain");
                }else if(domain && hideactive && hideObsolete){
                    let filteredData = data.filter(x => x["is_obsolete"] !== true)
                        .filter(x => x["activity_status"] === "active");
                    renderTable(sortByField(filteredData, "domain"), "domain");
                }else if(!domain && hideactive && hideObsolete){
                    let filteredData = data.filter(x => x["is_obsolete"] !== true)
                        .filter(x => x["activity_status"] === "active");
                    renderTable(filteredData, "");
                }
                else if(!domain && hideactive && !hideObsolete){
                    let filteredData = data["ontologies"].filter(x => x["activity_status"] === "active");
                    renderTable(filteredData, "");
                }
                else if(!domain && !hideactive && hideObsolete){
                    let filteredData = data.filter(x => x["is_obsolete"] !== true);
                    renderTable(filteredData, "");
                }
    }

    function Search(input, JsonData){
        let value = input.val().toLowerCase();
        if(value.length >= 2){
            return JsonData.filter((row)=>{
                let term = input.val().toLowerCase();
                if(row.domain === undefined){
                    row.domain = ""
                }
                if(row.description === undefined){
                    row.description = ""
                }
                return (row.id.toLowerCase().includes(term) ||
                    row.domain.toLowerCase().includes(term) ||
                    row.description.toLowerCase().includes(term))
                });
        }
        return JsonData;
    }
    function apply_all_filters(data){
        let selectedDomain = $("#dd-domains").children("option:selected").val();
                let res = data["ontologies"].filter(x => x["domain"] !== undefined);
                let dt = res.filter(x => x["domain"].includes(selectedDomain));
                let dt2 = Search($("#searchVal"), dt);
                applyFilters(dt2)
    }
    fetch('/registry/ontologies.jsonld')
        .then(response => response.json())
        .then( (data) => {

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
                attributes:    true,
                childList:     true,
                characterData: true
            });

            // extract domain and set values for drpdown menu
            let domains = [];
            for(let k=0; k<data["ontologies"].length; k++){
                if(data["ontologies"][k]["domain"] != undefined){
                    let d = data["ontologies"][k]["domain"] //.replace(" and", ",").split(",")
                    domains.push(d)
                }
            }
            domains = [...new Set(domains)];
            domains.sort();
            $("#dd-domains").append(`<option></option>`);
            domains.forEach(function (r){
                $("#dd-domains").append(`<option value="${r.trim()}">${r.trim()}</option>`);
            })
            //render unfiltered table
            renderTable(data["ontologies"]);

            // check box filter event for table data
            $("[data-filter]").on("change", () =>{
                apply_all_filters(data)
            });
            // get table by domain dropdown
            $("#dd-domains").on("change", () =>{
                apply_all_filters(data)

            });
            // search word in table
            $("#searchVal").on("keyup", debounce((e) => {
               apply_all_filters(data)
              }));

            let element = document.querySelector('[data-filter]');
            let event = new Event('change');
            element.dispatchEvent(event);
        }).catch(error => console.log(error));
});