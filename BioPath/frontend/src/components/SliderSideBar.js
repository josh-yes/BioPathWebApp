import React, { useEffect, useState } from 'react'

import "./css/SliderSideBar.css";
import "./css/stylesheet.css";

import dropdownLogo from "../icons/arrow-down-sign-to-navigate.png";


/**
 * Display and control concentration of pathway cofactors
 * @param props
 * @prop {Object[]} molecules
 * @prop molecules[].title
 * @prop molecules[].value
 * @prop handleConcentrationChange(string, int): void
 */
const SliderSideBar = (props) => {
    const handleSliderOpen = (cofactorTitle, newOpenStatus) => {
        if(newOpenStatus === true) {
        // close all others when another slider has been set to open
        }
    }

    const sliderItems = props.molecules.map((molecule) => 
        <li key={molecule.title}>
            <Slider 
                title={ molecule.title }
                value={ molecule.value.toFixed(2) }
                handleConcentrationChange={ props.handleConcentrationChange } 
            />
        </li>
    );

    return (
        <div className='card ModelAreaChild' id='PathwaySliderBox'>
            <button className="btn btn-primary" style={{margin: "10px"}} onClick={() => {props.run()}}>Run</button>
            <button className="btn btn-secondary" style={{margin: "10px"}} onClick={() => {props.stop()}}>Stop</button>
            <h3 id="sliderComponentTitle">{ props.slidersTitle }</h3>
            {( props.slidersDescription !== "") && <p><small className="text-muted">{ props.slidersDescription }</small></p> }
            <ul className='sliderBarList'>
                {sliderItems}
            </ul>
            
        </div>
    )
}

/**
 * Named slider selector
 * @prop title - title of the substrate passed in
 * @prop value
 * @prop handleConcentrationChange 
 */
const Slider = (props) => {
  let [isExpanded, setIsExpanded] = useState(false);

  const handleSliderValueChange = (newSliderValue) => {
    props.handleConcentrationChange(props.title, newSliderValue);
  }

  const handleClick = (e) => {
    setIsExpanded(!isExpanded);
  }

  const openHeader = 
        <ul id='cardHeaderList'>
            <li>
                <button className='cardHeaderDropdownButton' onClick={(e) => handleClick(e.target.value)}>
                    <img 
                        id='cardHeaderCaret' 
                        src={dropdownLogo} 
                    />
                </button>
            </li>
        <li><h5>{props.title}</h5></li>
        </ul>

    const closeHeader = 
        <button className='cardHeaderDropdownButton' onClick={(e) => handleClick(e.target.value)}>
            <ul id='cardHeaderList'>
            <li><img id='cardHeaderCaret' src={dropdownLogo} style={{ transform: "rotate(-90deg)"}}  /></li>
            <li><h5>{props.title}</h5></li>
            <li><small className="text-muted">{ props.value * 100 }%</small></li>
            </ul>
        </button>

    const cardContents = 
        <div className='card-body sliderCardContents'>
            <input 
                id="concentrationSlider"
                className='slider'
                type="range"
                min={0.0}
                step={0.1}
                max={2.0}
                onChange={(e) => handleSliderValueChange(e.target.value)}
                value={props.value}
            />
            <p className='card-text'>{parseInt(props.value * 100)}% of concentration</p> {/* parseInt because 110% was giving a long float */}
      </div>
      

  return (
    <div className='card growCard' id='sliderCard'>
      { isExpanded ? openHeader : closeHeader}
      { isExpanded ? cardContents : null }
    </div>
  )

}

export default SliderSideBar;