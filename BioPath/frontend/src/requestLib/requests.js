
// ----------------------------------------------------------------------
// requests.js
//  This file will contain a library of functions used to make 
//  requests to the backend
// 
//  each of the get functions will be returning JSON objects 
// ----------------------------------------------------------------------

// This will tell the functions where the data is coming from
//  This can be in the form of an API url for prod or a local file name for testing
//  Until we have the time to come up with a smarter, more automated solution where 
//  the data is being sourced from will need to be manually changed in the code

let BACKEND_BASE_API_URL = "http://localhost:8000/api/"; // API ACCESS
let LOCAL_STORAGE_PATH = "./sample-api/";         // LOCAL ACCESS
let MOCK_API_URL = "http://localhost:4000/api/";  // MOCK API ACCESS

let dataSourceAddress = BACKEND_BASE_API_URL;       // Choice Definition

// NOTE: the test suite for sample JSON will have a file structure matching the 
//   endpoints within the backend to keep calls consistent


function consoleLogRequestResults(status, statusText, endpointExtension, type, data) {
  // This helper function is here to standardize the print output of each request 
  // PARAMS:
  //  status: the status code of the request
  //  type: str describing type of request e.g. POST
  //  data: the JSON object sent or recieved (infered by type) 
  console.log(
    // "STATUS OF REQUEST: " + status + "\n" +
    // "STATUS TEXT: " + statusText + "\n" + 
    // "to endpoint: " + dataSourceAddress + endpointExtension + "\n" +
    // "type of request: " + type + "\n" +
    // "data: " + JSON.stringify(data) 
  );
}


/**
 * Requests pathway data from backend 
 * @param {int} id requested pathway id number
 * @returns response object from backend
 */
async function getPathwayById(id) {
  let endpointExtension = "pathways/" + id;
  let requestUrl = dataSourceAddress + endpointExtension;

  try {
    const response = await fetch(requestUrl, {
        headers: {
            "Content-Type": "application/json",
            // TODO: CHANGE HARD-CODED AUTH
            'Authorization': 'Basic ' + btoa("root:root")
        }
    });
    const isResponseJSON = response.headers.get('content-type')?.includes('application/json');
    const responseJSON = isResponseJSON && await response.json();

    // if it is a bad request throw an error
    if(!response.ok) {
      const error = (responseJSON && responseJSON.message) || response.status;
      throw error;
    }

    consoleLogRequestResults(
      response.status,
      response.statusText,
      endpointExtension,
      "GET",
      responseJSON
    );
    return responseJSON;

  } catch (error) {
    console.log(error);
    return error;
  }
}

async function getPathways() {
  const endpointExtension = "pathways/";
  const requestUrl = dataSourceAddress + endpointExtension;

  try {
    const response = await fetch(requestUrl, {
        headers: {
            "Content-Type": "application/json",
            // TODO: CHANGE HARD-CODED AUTH
            'Authorization': 'Basic ' + btoa("root:root")
        }
    });
    const isResponseJSON = response.headers.get('content-type')?.includes('application/json');
    const responseJSON = isResponseJSON && await response.json();
    
    // if it is a bad request throw an error
    if(!response.ok) {
      const error = (responseJSON && responseJSON.message) || response.status;
      throw error;
    }

    consoleLogRequestResults(
      response.status,
      response.statusText,
      endpointExtension,
      "GET",
      responseJSON
    );
    return responseJSON;

  } catch (error) {
    console.log(
      requestUrl + "\n" + 
      error
    );
    return error;
  }
}


async function postPathway(pathwayObj) {
  const methodType = "POST";
  const endpointExtension = "pathways/";
  const requestUrl = dataSourceAddress + endpointExtension;

  try {
    const requestOptions = {
      method: methodType,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(pathwayObj)
    };

    const response = await fetch(requestUrl, requestOptions);
    const isResponseJSON = response.headers.get('content-type')?.includes('application/json');
    const responseJSON = isResponseJSON && await response.json();
    
    // if it is a bad request throw an error
    if(!response.ok) {
      const error = (responseJSON && responseJSON.message) || response.status;
      throw error;
    }

    consoleLogRequestResults(
      response.status,
      response.statusText,
      endpointExtension,
      methodType,
      responseJSON
    );
    return responseJSON;
  } catch(error) {
    console.log(
      requestUrl + "\n" + 
      error
    );
    return error;
  }
}

export { getPathways, getPathwayById, postPathway }