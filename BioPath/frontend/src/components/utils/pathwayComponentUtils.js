/* basic function where if concentration[i] greater than previous you subtract
from i - 1 and add to i
*/
export function runConcentrations (concentrations, filled) {
    for (let i = 0; i < concentrations.length; i++) {
        if (i > 0) { 
            // if concentrations are not first or last egde
            if (concentrations[i - 1] < 5) { // concentration to low for reaction to occur
                concentrations[i] = 0;
            }
            else if (concentrations[i - 1] > concentrations[i]) {
                concentrations[i-1] = concentrations[i-1] - .05;
                concentrations[i] = concentrations[i] + .05;
            }
            else if (concentrations[i - 1] < concentrations[i]) { // TODO:
                // if reaction is reversible, molecule at (i) converted to molecule at (i-1)
            }
        }
    }
    return concentrations;
}

/* function that deals with reversible reaction
*/
export function run (concentrations, reversibleSteps, factors, factorSteps) {
    
    for (let i = 0; i < concentrations.length; i++) {
        if (factorSteps.includes(i)) { // dependent on cofactor
            if (i === 0) { // starting step
                concentrations[i] += .01; // always add constant value to start
                if (factors[factorSteps.indexOf(i)] > 0) { // if cofactor present
                    concentrations[i]-= .01 * factors[factorSteps.indexOf(i)];
                }
            }
            else if (i < concentrations.length - 1) { // middle steps
                if (concentrations[i - 1] >= concentrations[i]) { // flows down
                    concentrations[i] += .01 * factors[factorSteps.indexOf(i)];
                    if (concentrations[i - 1] !== 0) { // check if 0 because 0 already subtracted
                        concentrations[i - 1] -= .01 * factors[factorSteps.indexOf(i)];
                    }
                }
                else if (reversibleSteps.includes(i)) { // it is a reversible step
                    concentrations[i] -= .01 * factors[factorSteps.indexOf(i)];
                    concentrations[i - 1] += .01 * factors[factorSteps.indexOf(i)];
                }
            }
            else { // last step in pathway
                if (concentrations[i - 1] > concentrations[i]) { // flows down
                    concentrations[i - 1] -= .01 * factors[factorSteps.indexOf(i)];
                    concentrations[i] += .01 * factors[factorSteps.indexOf(i)];
                    concentrations[i] -= .01; // always substract constant value from end
                }
            }
        }
        else {
            if (i === 0) { // infinite first substrate
                concentrations[i] = concentrations[i] + .01;
            }
            else if (i < concentrations.length - 1) { // all must last substrate
                if (concentrations[i - 1] > concentrations[i]) { // flows down
                    concentrations[i - 1] = concentrations[i - 1] - .01;
                    concentrations[i] = concentrations[i] + .01;
                }
                else if (reversibleSteps.includes(i)) { // reversible step
                    concentrations[i] -= .01;
                    concentrations[i - 1] += .01;
                }
            }
            else { // last substrate subtract so it doesnt get infinitely bigger
                concentrations[i] = concentrations[i] - .01;
            }
        }
    }
    return concentrations;
}


/**
 Build a flow model from pathway json
*/ 
export function buildFlow(pathway) {
    // these are mocked for testing fix later
    if(typeof pathway === "undefined" || typeof pathway.enzymes === "undefined") { 
        console.log("buildFlow: Invalid pathway passed");
        return;
    }
    // MAKING CHANGE TO DICTIONARY LIKE THIS TO HELP READBILITY
    return {"nodes": generateNodes(pathway), "edges": generateEdges(pathway)};
}

/**
 * Generates ReactFlow edges between enzyme and molecule nodes
 * @param {*} pathway
 */
export function generateEdges(pathway) {
    let edges = [];
    for (const enzyme of pathway.enzymes) {
        // Make edge from substrate to enzyme
        for (const substrate_id of enzyme.substrates) {
            edges.push({
                id: String(substrate_id) + "_" + String(enzyme.id),
                data: {
                    "title": String(substrate_id) + " to " + String(enzyme.id),
                    "molecule_id": String(substrate_id)
                },
                animated: true,
                source: String(substrate_id) + "_molecule",
                target: String(enzyme.id) + "_enzyme"
            });
            if (enzyme.reversible) {
                /* 
                edges.push({
                    id: String(substrate_id) + "_" + String(enzyme.id),
                    data: {
                        "title": String(substrate_id) + " to " + String(enzyme.id),
                        "molecule_id": String(substrate_id)
                    },
                    animated: true,
                    source: String(enzyme.id) + "_enzyme",
                    target: String(molecule_id) + "_molecule"
                });
                */
            }
        }
        // Make edge from enzyme to product
        for (const product_id of enzyme.products) {
            edges.push({
                id: String(enzyme.id) + "_" + String(product_id),
                data: {
                    "title": String(product_id) + " to " + String(enzyme.id),
                    "molecule_id": String(product_id)
                },
                animated: true,
                source: String(enzyme.id) + "_enzyme",
                target: String(product_id) + "_molecule"
            });
        }
    }
    return edges;
}

/**
    Function to parse the pathway JSON into reactflow nodes

    @param pathway Pathway object retrieved from backend
    @return lists of nodes to be used by ReactFlow
*/
export function generateNodes(pathway) {
    if(typeof pathway === "undefined" || typeof pathway.enzymes === "undefined") { 
        console.log("generateNodes: Invalid pathway passed");
        return;
    }
    let nodes = []

    for (const enzyme of pathway.enzymes) {
        // Reactflow node
        nodes.push({
            id: String(enzyme.id) + "_enzyme", 
            className: 'enzyme', 
            data: {
                label: enzyme.name, 
                type: "enzyme",
                reversible: enzyme.reversible,
                substrates: enzyme.substrates, 
                products: enzyme.products
            },
            position: {x: enzyme.x, y: enzyme.y}
        });
    }
    
    for (const molecule of pathway.molecules) {
        // Reactflow node
        nodes.push({
            id: String(molecule.id) + "_molecule", 
            className: 'substrate', 
            data: {
                label: molecule.name,
                type: "molecule",
                title: molecule.name,
                concentration: 100
            },
            position: {x: molecule.x, y: molecule.y}
        });
    }
    return nodes;
}

/**
    This function is used to parse through the pathway JSON.
    It loops through each enzyme and if there are cofactors it adds
    the cofactor name to a list that is returned
*/
export function findSliders(pathwayData) {
    let sliders = []; // list of cofactors extracted from pathway JSON
    let percent = []; // new

    for (let i = 0; i < pathwayData.enzymes.length; i++) {
        if (pathwayData.enzymes[i].cofactors.length > 0) { // if cofactor exists
            for (const cofactor of pathwayData.enzymes[i].cofactors) { // add each cofactor
                if (!sliders.includes(cofactor)) { // only add unique cofactors
                    sliders.push(cofactor);
                    percent.push(1); // new
                }
                else {
                    console.log(cofactor + " already exists in slider list");
                }
            }
        }
    }
    
    return {
        "sliders": sliders,
        "percent": percent
    };
}


/**
    Function to generate the molecules that will be tracked in a pathway
    returns the list of molecules and their corresponding concentrations
    All molecules start with the same baseConcentration

    pathwayData is the JSON passed in
    baseConcentration is a value that will set the base concentration 
        for each molecule (optional) 100 is default
*/
export function findMolecules(pathwayData, baseConcentration=10) {
    let molecules = [];
    let concentrations = [];

    for (const molecule of pathwayData.molecules) {
        // probably need to add some error checking like a molecule without name
        // might need to switch to id instead of name depending on how we do JSON
        molecules.push(molecule.id);
        concentrations.push(baseConcentration);
    }

    return {
        "molecules": molecules, 
        "concentrations": concentrations
    };
}

/**
 * Parses a list of enzyme data from pathway data
 * @param pathwayData data from backend
 * @returns list of enzymes with substrates, products, and cofactors
 */
export function parseEnzymesForSliders(pathwayData) {
    let enzymes = [];
    for (const enzyme of pathwayData.enzymes) {
        let e = {
            "substrates": [],
            "products": [],
            "cofactors": []
        }

        // Get abbreviations for molecule IDs
        for (const substrate of enzyme["substrates"]) {
            let m = pathwayData["molecules"].filter(o => {
                return o.id === substrate;
            });
            if (m.length > 0) {
                e["substrates"].push(m[0]["abbreviation"]);
            }
        }
        for (const product of enzyme["products"]) {
            let m = pathwayData["molecules"].filter(o => {
                return o.id === product;
            });
            if (m.length > 0) {
                e["products"].push(m[0]["abbreviation"]);
            }
        }
        for (const cofactor of enzyme["cofactors"]) {
            let m = pathwayData["molecules"].filter(o => {
                return o.id === cofactor;
            });
            if (m.length > 0) {
                e["cofactors"].push(m[0]["abbreviation"]);
            }
        }
        enzymes.push(e);
    }
    return enzymes;
}