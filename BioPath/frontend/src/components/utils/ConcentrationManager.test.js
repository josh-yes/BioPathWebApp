import ConcentrationManager from "./ConcentrationManager";

describe('concentrations', () => {
    test('init', () => {
        let enzymes = [
            {
                substrates: ["G"],
                products: ["G6"],
                cofactors: ["Na"]
            }
        ]
        let c = new ConcentrationManager();
        c.parseEnzymes(enzymes);
        expect(c.moleculeConcentrations["G"]).toBe(1);
        expect(c.moleculeConcentrations["G6"]).toBe(1);
        expect(c.moleculeConcentrations["Na"]).toBe(1);
    });
    
    test('update', () => {
        let enzymes = [
            {
                substrates: ["G"],
                products: ["G6"],
                cofactors: ["Na"]
            }
        ]
        let c = new ConcentrationManager();
        c.parseEnzymes(enzymes);
        c.updateConcentrations();
        expect(c.moleculeConcentrations["G"]).toBe(0.9);
        expect(c.moleculeConcentrations["G6"]).toBe(1.1);
    });
    
    test('addListener', () => {
        let enzymes = [
            {
                substrates: ["G"],
                products: ["G6"],
                cofactors: ["Na"]
            }
        ]
        let c = new ConcentrationManager();
        c.parseEnzymes(enzymes);
        let listener = jest.fn();
        c.addListener(listener);
        c.updateConcentrations();
        expect(listener).toHaveBeenCalled();
    });

    test('removeListener', () => {
        let enzymes = [
            {
                substrates: ["G"],
                products: ["G6"],
                cofactors: ["Na"]
            }
        ]
        let c = new ConcentrationManager();
        c.parseEnzymes(enzymes);
        let listener_a = jest.fn();
        c.addListener(listener_a);
        c.updateConcentrations();
        c.removeListener(listener_a);
        c.updateConcentrations;
        expect(listener_a).toHaveBeenCalledTimes(1);     
    });

    test('setConcentration', () => {
        let enzymes = [
            {
                substrates: ["G"],
                products: ["G6"],
                cofactors: ["Na"]
            }
        ]
        let c = new ConcentrationManager();
        c.parseEnzymes(enzymes);
        let listener_a = jest.fn();
        c.addListener(listener_a);
        c.setConcentration("G", 0.2);
        expect(c.moleculeConcentrations["G"]).toBe(0.2);
        expect(listener_a).toHaveBeenCalledTimes(1);
    });
});
