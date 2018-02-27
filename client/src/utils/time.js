/**
 * Utility function to calculate timeout in miliseconds
 * @param  {number} timeout             Default timeout in seconds
 * @param  {number} delta               Delta time (+/-) in seconds
 * @returns {number}                    Timeout + delta (in miliseconds)
 */
export const timeoutDelta = (t, delta = 0) => (t + delta) * 1000;
