import React from 'react'
import parkingSlotIcon from './static/parkingSlotIcon.svg' 
import mapMarker from './static/mapMarker.svg'
import parkingSearchIcon from './static/parkingSearchIcon.svg'

export function BuildingCard ({building}) {
    const buildingName = building.name
    const address = building.address
    const availableSlots = building.number_of_available_slots
    const image = building.image_url
    return (
        <>  
                <div className='bc'>
                    <div className="bc-body">
                        <div className="bc-body-lotImageContainer">
                            <img src={image} className='bc-body-lotImageContainer-image' alt={`${buildingName} logo`} />
                        </div>
                    </div>

                    <aside className="bc-aside">
                        <h1 className="bc-aside-name">
                            {buildingName}
                        </h1>
                       
                        <h2 className="bc-aside-address">
                            <div>
                                <img src={mapMarker} alt="" className='bc-aside-address-img'/> 
                            </div>
                            <div className="bc-aside-address-text">
                                {address}
                            </div>
                        </h2>
                        <div className='bc-aside-slots'>
                            <div className='bc-aside-slots-info'>
                                <div>
                                <img src={parkingSlotIcon} alt="Slot icon" className='bc-aside-slots-slotIcon'/> 
                                </div>
                                <div className='bc-aside-slots-slotNumber'>
                                        {availableSlots}
                                </div>
                            </div>
                            <div className='bc-aside-slots-buttonContainer'>
                                <button className='bc-aside-slots-searchButton'>
                                        <img className='bc-aside-slots-searchButton-img' src={parkingSearchIcon} alt="" />
                                </button>
                            </div>
                        </div>
                        
                    </aside> 
                </div>
        </>
        )
    }