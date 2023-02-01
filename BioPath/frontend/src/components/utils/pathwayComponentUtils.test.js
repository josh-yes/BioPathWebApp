import { parseEnzymesForSliders } from "./pathwayComponentUtils";

describe('pathwayComponentUtils', () => {
    test('parseEnzymesForSliders', () => {
        let data = {
            "enzymes":[{
                "id":24,
                "name":"enzyme1",
                "abbreviation":"e1",
                "reversible":true,
                "substrates":[56],
                "products":[57],
                "cofactors":[58]
            }], 
            "molecules":[{
                "id":56,
                "abbreviation":"m1"
            },{
                "id":57,
                "abbreviation":"m2"
            },{
                "id":58,
                "abbreviation":"m3",
            }]
        }
        let enzymes = parseEnzymesForSliders(data);
        expect(enzymes.length).toEqual(1);
        for (const e of enzymes) {
            expect(e["substrates"]).toContain("m1");
            expect(e["products"]).toContain("m2");
            expect(e["cofactors"]).toContain("m3");
        }
    });
});