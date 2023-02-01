import React from 'react';
import { MarkerType, Position } from 'reactflow';

const groupHeight = 130;
const groupWidth1 = 120;
const groupWidth2 = 230;
const substrateHeight = 50
const substrateWidth = 100

export const nodes = [
    { 
    id: '1e',
    position: { x: 0, y: (groupHeight + 20) * 0 },
    data: {label: 'Hexokinase'},
    type: 'group',
    className: 'enzyme',
    style: {
        width: groupWidth2,
        height: groupHeight,
    },
    },
    { 
    id: '2e',
    position: { x: 0, y: (groupHeight + 20) * 1 },
    data: {label: ''},
    type: 'group',
    className: 'enzyme',
    style: {
        width: groupWidth1,
        height: groupHeight,
    },
    },
    { 
    id: '3e',
    position: { x: 0, y: (groupHeight + 20) * 2 },
    data: {label: null},
    type: 'group',
    className: 'enzyme',
    style: {
        width: groupWidth2,
        height: groupHeight,
    },
    },
    { 
    id: '4e',
    position: { x: 0, y: (groupHeight + 20) * 3 },
    data: {label: null},
    type: 'group',
    className: 'enzyme',
    style: {
        width: groupWidth2,
        height: groupHeight,
    },
    },
    { 
    id: '5e',
    position: { x: substrateWidth + 10, y: (groupHeight + 20) * 4 },
    data: {label: null},
    type: 'group',
    className: 'enzyme',
    style: {
        width: groupWidth1,
        height: groupHeight,
    },
    },
    { 
    id: '6e',
    position: { x: 0, y: (groupHeight + 20) * 5 },
    data: {label: null},
    type: 'group',
    className: 'enzyme',
    style: {
        width: groupWidth2,
        height: groupHeight,
    },
    },
    { 
    id: 'starts',
    position: { x: 10, y: -70 },
    data: { label: 'Glucose' },
    className: 'substrate',
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    {
    id: '1s',
    position: { x: 10, y: 10 },
    data: { label: 'Glucose' },
    className: 'substrate',
    parentNode: '1e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    { 
    id: '2s',
    position: { x: 10, y: substrateHeight + 20 },
    data: { label: 'G6P' },
    className: 'substrate',
    parentNode: '1e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    {
    id: '1sc',
    position: { x: substrateWidth + 20, y: 10 },
    data: { label: 'ATP' },
    className: 'substrate',
    parentNode: '1e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    { 
    id: '2sc',
    position: { x: substrateWidth + 20, y: substrateHeight + 20 },
    data: { label: 'ADP' },
    className: 'substrate',
    parentNode: '1e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    { 
    id: '3s',
    position: { x: 10, y: 10 },
    data: { label: 'G6P' },
    className: 'substrate',
    parentNode: '2e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    {
    id: '4s',
    position: { x: 10, y: substrateHeight + 20 },
    data: { label: 'F6P' },
    className: 'substrate',
    parentNode: '2e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    {
    id: '5s',
    position: { x: 10, y: 10 },
    data: { label: 'F6P' },
    className: 'substrate',
    parentNode: '3e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    {
    id: '6s',
    position: { x: 10, y: substrateHeight + 20 },
    data: { label: 'F1,6BP' },
    className: 'substrate',
    parentNode: '3e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    {
    id: '3sc',
    position: { x: substrateWidth + 20, y: 10 },
    data: { label: 'ATP' },
    className: 'substrate',
    parentNode: '3e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    { 
    id: '4sc',
    position: { x: substrateWidth + 20, y: substrateHeight + 20 },
    data: { label: 'ADP' },
    className: 'substrate',
    parentNode: '3e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    { 
    id: '7s',
    position: { x: 10, y: 10 },
    data: { label: 'F1,6BP' },
    className: 'substrate',
    parentNode: '4e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    { 
    id: '8s',
    position: { x: 10, y: substrateHeight + 20 },
    data: { label: 'GH3P'},
    className: 'substrate',
    parentNode: '4e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    { 
    id: '8s2',
    position: { x: substrateWidth + 20, y: substrateHeight + 20 },
    data: { label: 'DHAP' },
    className: 'substrate',
    parentNode: '4e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    { 
    id: '9s',
    position: { x: 10, y: 10 },
    data: { label: 'DHAP' },
    className: 'substrate',
    parentNode: '5e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    { 
    id: '10s',
    position: { x: 10, y: substrateHeight + 20 },
    data: { label: 'GH3P' },
    className: 'substrate',
    parentNode: '5e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    { 
    id: '11s',
    position: { x: 10, y: 10 },
    data: { label: 'GH3P' },
    className: 'substrate',
    parentNode: '6e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    { 
    id: '12s',
    position: { x: 10, y: substrateHeight + 20 },
    data: { label: '1,3BPG' },
    className: 'substrate',
    parentNode: '6e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    {
    id: '5sc',
    position: { x: substrateWidth + 20, y: 10 },
    data: { label: 'NAD' },
    className: 'substrate',
    parentNode: '6e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    { 
    id: '6sc',
    position: { x: substrateWidth + 20, y: substrateHeight + 20 },
    data: { label: 'NADH' },
    className: 'substrate',
    parentNode: '6e',
    extent: 'parent',
    draggable: false,
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
    { 
    id: 'ends',
    position: { x: 10, y: (groupHeight + 20) * 6 },
    data: { label: '1,3BPG' },
    className: 'substrate',
    style: {
        width: substrateWidth,
        height: substrateHeight,
    },
    },
];

export const edges = [
    {
    // id: 'starts-1s',
    id: 'Glucose',
    data: 'Glucose',
    source: 'starts',
    target: '1s',
    animated: true,
    style: {
        strokeWidth: 10,
        // strokeWidth: getConc(),
        stroke: 'red'
    }
    },
    {
    // id: '2s-3s',
    id: 'G6P',
    data: 'G6P',
    source: '2s',
    target: '3s',
    animated: true,
    style: {
        strokeWidth: 10,
        stroke: 'red'
    }
    },
    {
    // id: '4s-5s',
    id: 'F6P',
    data: 'F6P',
    source: '4s',
    target: '5s',
    animated: true,
    style: {
        strokeWidth: 10,
        stroke: 'red'
    }
    },
    {
    // id: '6s-7s',
    id: 'F1,6BP',
    data: 'F1,6BP',
    source: '6s',
    target: '7s',
    animated: true,
    style: {
        strokeWidth: 10,
        stroke: 'red'
    }
    },
    {
    // id: '8s2-9s',
    id: 'DHAP',
    data: 'DHAP',
    source: '8s2',
    target: '9s',
    animated: true,
    style: {
        strokeWidth: 10,
        stroke: 'red'
    }
    },
    {
    id: '10s-11s',
    // id: '1,3BPG',
    data: 'GH3P',
    source: '10s',
    target: '11s',
    animated: true,
    style: {
        strokeWidth: 10,
        stroke: 'red'
    }
    },
    {
    id: 'GH3P',
    data: 'GH3P',
    source: '8s',
    target: '11s',
    animated: true,
    style: {
        strokeWidth: 10,
        stroke: 'red'
    }
    },
    {
    id: '1,3BPG',
    data: '1,3BPG',
    source: '12s',
    target: 'ends',
    animated: true,
    style: {
        strokeWidth: 10,
        stroke: 'red'
    }
    },

];