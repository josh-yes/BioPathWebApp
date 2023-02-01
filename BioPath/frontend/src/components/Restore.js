import React, { useState, useCallback, useEffect } from 'react';
import ReactFlow, {
    ReactFlowProvider,
    useNodesState,
    useEdgesState,
    addEdge,
    useReactFlow,
} from 'reactflow';
import 'reactflow/dist/style.css';

// import {nodes as initialnodes} from './simpleJSON';
import { runConcentrations, run, run2 } from './utils/pathwayComponentUtils';
import {buildFlow, buildNodes, generateNodes} from './utils/pathwayComponentUtils';

import './css/Restore.css';

const flowKey = 'example-flow';

const getNodeId = () => `randomnode_${+new Date()}`;

// const initialNodes = [
//     { id: '1', data: { label: 'Node 1' }, position: { x: 100, y: 100 } },
//     { id: '2', data: { label: 'Node 2' }, position: { x: 100, y: 200 } },
// ];

// const initialEdges = [{ id: 'e1-2', source: '1', target: '2' }];


const SaveRestore = (props) => {
    // generateNodes();
    var initial = buildFlow();
    const initialNodes = initial[0];
    const initialEdges = initial[1];
    const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
    const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);
    const [rfInstance, setRfInstance] = useState(null);
    const { setViewport } = useReactFlow();

    console.log(props.titles, "dog");

    var [concentrations, setConcentrations] = useState(props.concentration); // new

    const onConnect = useCallback((params) => setEdges((eds) => addEdge(params, eds)), [setEdges]);

    useEffect(() => {
        // setConcentrations((conc) => 
        //     concentrations = runConcentrations(props.concentration)
        // );
        console.log(props.concentration, "hello");
        // setEdges((eds) =>
        //     eds.map((edge) => {
        //     // for loop is needed for edges that have the same input, ex. GH3P
        //     // O(N^2) so might need to change if its too slow for later pathways
        //     for (let i = 0; i < props.concentration.length; i++) {
        //         if (edge.data == props.title[i]) {
        //         // edge.style = {strokeWidth: props.concentration[i], stroke: 'red'};
        //             if (props.factorSteps.includes(i)) { // is a factor step
        //                 edge.style = {strokeWidth: concentrations[i], stroke: 'yellow'};
        //             }
        //             else {
        //                 edge.style = {strokeWidth: concentrations[i], stroke: 'red'};
        //             }
        //         }
        //     }
    
        //     return edge;
        //     })
        // );
    }, [props.concentration, setEdges]);

    const onSave = useCallback(() => {
        if (rfInstance) {
            const flow = rfInstance.toObject();
            localStorage.setItem(flowKey, JSON.stringify(flow));
        }
    }, [rfInstance]);

    const onRestore = useCallback(() => {
        const restoreFlow = async () => {
        const flow = JSON.parse(localStorage.getItem(flowKey));

            if (flow) {
                const { x = 0, y = 0, zoom = 1 } = flow.viewport;
                setNodes(flow.nodes || []);
                setEdges(flow.edges || []);
                setViewport({ x, y, zoom });
            }
        };

        restoreFlow();
    }, [setNodes, setViewport]);

    const onAdd = useCallback(() => {
        const newNode = {
        id: getNodeId(),
        data: { label: 'Added node' },
        position: {
            x: Math.random() * window.innerWidth - 100,
            y: Math.random() * window.innerHeight,
        },
        };
        setNodes((nds) => nds.concat(newNode));
    }, [setNodes]);

    const onClear = useCallback(() => {
        localStorage.clear();
        setNodes(initialNodes);
        setEdges(initialEdges);
    }, [setNodes, setViewport])

    return (
        <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        onInit={setRfInstance}
        >
        <div className="save__controls">
            <button onClick={onSave}>save</button>
            <button onClick={onRestore}>restore</button>
            <button onClick={onAdd}>add node</button>
            <button onClick={onClear}>clear flow</button>
        </div>
        </ReactFlow>
    );
};

export default () => (
    <ReactFlowProvider>
        <SaveRestore />
    </ReactFlowProvider>
);