// usage:
// describe('getTimestamp', () => {
//   const RealDate = Date;

//   afterEach(() => {
//     global.Date = RealDate;
//   });

//   it('should return timestamp', () => {
//     mockDate('2017-11-25T12:34:56z');
//     expect(getTimestamp()).toEqual('20171125123456');
//   });
// });

function mockDate(isoDate) {
  global.Date = class extends Date {
    constructor() {
      return new Date(isoDate);
    }
  };
}

export default mockDate;
