class BaseController:
  def update(self, target_lataccel, current_lataccel, state):
    raise NotImplementedError


class OpenController(BaseController):
  def update(self, target_lataccel, current_lataccel, state):
    return target_lataccel


class SimpleController(BaseController):
  def update(self, target_lataccel, current_lataccel, state):
    return (target_lataccel - current_lataccel) * 0.3

class SimpleController2(BaseController):
  def update(self, target_lataccel, current_lataccel, state):
    return 0.5*target_lataccel - 0.1*current_lataccel - 0.35* state.roll_lataccel

CONTROLLERS = {
  'open': OpenController,
  'simple': SimpleController,
  'simple2': SimpleController2, 
}
