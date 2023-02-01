


// class PathwayInteractiveComponent extends Component {
//   constructor(props) {
//     if(this.constructor === PathwayInteractiveComponent) {
//       throw new Error("Abstract PathwayInteractiveComponent cannot be instantiated directly");
//     }
    
//     this.eventTypeId = "";
//   }

// }


// ----------------------------------------------------------------------
// userInputInteractionList
//  It will be the interface the pathway model will use to interact with
//    the user's input
//  This list will coordinate and hold all user input sources and map
//    them (one to many) to any observers which rely on that data within
//    the pathway
// ----------------------------------------------------------------------
export default class userInputInteractionList {
  constructor() {
    //-------------------------------------------------------------------
    // DEFINED TYPES:
    //  List of all defined event messages that can be passed for now
    //  This data should be attached to the data object you are working 
    //  with so you shouldnt have to explicitly write it out each time
    //  IF YOU ARE WRITING A RAW STRING IN postEvent() PARAMATERS, 
    //    YOU'RE DOING IT WRONG 
    //
    // List:
    //  - "concentrationChange"
    //  - "loadPathway"
    //  - "closePathway"
    //
    // NOTE: this should be added to if more event types are needed
    //       as convention, their names should be what they return
    //-------------------------------------------------------------------


    // SUBSCRIBERS LIST 
    // this dictionary will map:
    //  (eventType) : [eventHandlerFunctions]
    // it will be used to make the conversion from a 
    this.observerMapping = {};
  }

  // when an event is posted on a change to an input item
  //  this function should read through all handlers connected to 
  //  the event type reported and trigger them
  // FOR EXAMPLE:
  //  If a slider is changed, have it call post event with an Id specifying 
  //  its specific event where it can find said event which will handle 
  //  making the changes needed in the pathway
  postEvent(eventTypeId, jsonData) {
    let handlers = this.observerMapping[eventTypeId]

    if(typeof handlers === "undefined") {
      console.log("postEvent called with undefined handler");
      return;
    }
    else if(handlers === null || handlers.length === 0) {
      console.log("postEvent called but handlers are empty");
      return;
    }
    else {
      let mappedToFunctions = this.observerMapping[eventTypeId];

      for (const handlerFunction of mappedToFunctions) {
          handlerFunction(jsonData)
      }
    }
  }


  subscribe(eventTypeId, eventHandlerFunction) {
    if(eventTypeId in this.observerMapping){
      this.observerMapping[eventTypeId].push(eventHandlerFunction);
    }
    else {
      this.observerMapping[eventTypeId] = [eventHandlerFunction];
    }
  }
}