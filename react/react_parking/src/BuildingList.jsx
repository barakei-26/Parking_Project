import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { BuildingCard } from './BuildingCard';

export function BuildingList () {
    const [buildingList, setBuildingList] = useState([]);
    const buildingListUrl = 'http://127.0.0.1:8000/api/building/all';

    useEffect(() => {
        axios.get(buildingListUrl)
            .then(response => {
                const serializedBuildingList = response.data; // Fetching data properly
                setBuildingList(serializedBuildingList); // Update state with the fetched data
            })
            .catch(error => console.log(error));
    }, []);

    return (
        <>
                {buildingList.map((building, index) => (
                    <React.Fragment key={index}>
                         <BuildingCard  building={building}></BuildingCard>
                    </React.Fragment>
                ))}
        </>
    );
}
