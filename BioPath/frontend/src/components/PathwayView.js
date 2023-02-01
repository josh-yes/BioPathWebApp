import React, { Component, useState, useEffect } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import FlowModel from './FlowModel'
import NavBar from './NavBar'
//import RightSideBarArea from './RightSideBarArea';
import Error from "./Error";

//import Restore from './Restore';
import './css/PathwayView.css'


//import { buildFlow, findMolecules, findSliders } from './utils/pathwayComponentUtils';
import userInputInteractionList from './PathwayInteractiveComponent';
import ConcentrationManager from './utils/ConcentrationManager';

export default class PathwayView extends Component {
  constructor(props) {
    super(props);

    // this.handleConcChange = this.handleConcChange.bind(this)

    // setup observers for all inputs which affect the pathway 
    //  this observer list will be passed into each of the non-modelArea 
    //  components
    this.pathwayUserInputSubList = new userInputInteractionList();
    this.concentrationManager = new ConcentrationManager();
  }

  render() {
    const pathwayView = <div className="container-fluid" id='MainView'>
                          <div className="row" id="NavBarRow">
                            <NavBar />
                          </div>

                          {/* the pathway view, left, and right sidebar divs are going to 
                              be held in columns
                          */}
                          <div className="row" id="PathwayViewRow">
                            <div className="col" id="ModelAreaCol">
                              <FlowModel 
                                concentrationManager= {this.concentrationManager}
                              />
                              
                            </div>

                            {/* <div className="col-md-auto" id="RightSideBarAreaCol">
                              <RightSideBarArea dataObserver={ this.pathwayUserInputSubList }/>
                            </div> */}
                          </div>
                        </div>

    return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={ pathwayView }>
            <Route path="pathway/:pathwayID" element={ pathwayView }/>
          </Route>

          {/* for user authentication later on,  */}
          <Route path="auth" element={ pathwayView }>
          </Route>
          <Route path="*" element={ <Error /> }/>
        </Routes>
      </BrowserRouter>
    )
  }
}

