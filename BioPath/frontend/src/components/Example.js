import React, {useEffect, useState } from 'react'

const Example = (props) => {
    let [data, setData] = useState("data");

    useEffect(() => {
        console.log(data);
    }, [data]);

    return(
        <div>
            <p>Example</p>
        </div>
    );
}

export default Example;