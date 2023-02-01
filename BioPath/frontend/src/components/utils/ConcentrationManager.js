/**
 * Manages concentrations of a model and
 * notifies any listeners on concentration change
 * @class
 * @classdesc Managing model concentrations for
 * real time web app.
 * 
 * @author zburnaby
 */
class ConcentrationManager {
    /**
     * @constructor
     */
    constructor() {
        this.moleculeConcentrations = [];
        this.enzymes = [];
        this.listeners = [];
        this.interval = null;
    }

    /**
     * Initializes the molecule_concentrations list given some enzymes
     * @function
     * @param {Object[]} enzymes list of enzymes
     * @param enzymes[].substrates list of input moleules to the enzyme
     * @param enzymes[].products list of output molecules to the enzyme
     * @param enzymes[].cofactors list of molecules effecting the enzyme's production
     */
    parseEnzymes(enzymes) {
        this.moleculeConcentrations = [];
        for (const enzyme of enzymes) {
            for (const substrate of enzyme.substrates) {
                this.moleculeConcentrations[substrate] = 1;
            }
            for (const product of enzyme.products) {
                this.moleculeConcentrations[product] = 1;
            }
            for (const cofactor of enzyme.cofactors) {
                this.moleculeConcentrations[cofactor] = 1;
            }
        }
        this.enzymes = enzymes;
        // for (let enzyme of this.enzymes) {
        //     console.log(enzyme);
        // }
        // for (const m in this.moleculeConcentrations) {
        //     console.log(m + ":" + this.moleculeConcentrations[m]);
        // }
        this.notifyListeners();
    }

    /**
     * Updates the concentrations of each molecule
     * @function
     */
    updateConcentrations() {
        let cachedConcentrations = this.moleculeConcentrations;
        for (const enzyme of this.enzymes) {
            let minSubstrateConc = null;
            for (const substrate of enzyme.substrates) {
                if (!minSubstrateConc) {
                    minSubstrateConc = cachedConcentrations[substrate];
                }
                if (cachedConcentrations[substrate] < minSubstrateConc) {
                    minSubstrateConc = cachedConcentrations[substrate];
                }
            }
            for (const substrate of enzyme.substrates) {
                if (minSubstrateConc) {
                    this.moleculeConcentrations[substrate] -= minSubstrateConc * 0.1;
                }
            }
            for (const product of enzyme.products) {
                if (minSubstrateConc) {
                    this.moleculeConcentrations[product] += minSubstrateConc * 0.1;
                }
            }
        }
        console.log("UpdateConcentrations()");
        this.notifyListeners();
    }

    /**
     * Passes current molecule concentrations to all listening functions
     * @function
     */
    notifyListeners() {
        for (const listener of this.listeners) {
            listener(this.moleculeConcentrations);
        }
    }

    /**
     * @callback onUpdateConcentration
     * @param {Object[]} moleculeConcentrations
     */

    /**
     * Add listener function from listener queue
     * @function
     * @param {onUpdateConcentration} listener
     */
    addListener(listener) {
        this.listeners.push(listener);
    }

    /**
     * Remove listener function from listener queue
     * @function
     * @param {onUpdateConcentration} listener
     */
    removeListener(listener) {
        for (let i = 0; i < this.listeners.length; i++) {
            if (this.listeners[i] === listener) {
                this.listeners.splice(i, 1);
            }
        }
    }

    /**
     * Manually set the concentration of a molecule
     * @param {string} title 
     * @param {int} value 
     */
    setConcentration(title, value) {
        if (this.moleculeConcentrations) {
            this.moleculeConcentrations[title] = parseFloat(value);
            this.notifyListeners();
        } else {
            console.log("No Concentrations");
        }
    }

    getMolculeConcentrations() {
        return this.moleculeConcentrations;
    }
}

export default ConcentrationManager;