import unavailableSvg from './static/unavailable.svg'; 
import availableSvg from './static/available.svg'

export function SlotCard ({isAvailable, slotId}) {
    const imageSrc = isAvailable ? availableSvg : unavailableSvg;
    const buttonText = isAvailable ? 'Reserve' : 'Ocuppied'; 

    return(
        <article className='pk-slotCard'>
                <div className='pk-slotCard-content'>
                    <h1 className='pk-slotCard-tittle'>{slotId}</h1>
                    <img className='pk-slotCard-img' src={imageSrc} alt='Unavailable slot'/>  
                    <button className='pk-slotCard-reservationButton'> {buttonText} </button>
                </div>
        </article>
        
    );
}